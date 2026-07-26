from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

import httpx
import pytest
from pydantic import ValidationError

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper

_FEED = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"><channel><title>Test</title>
  <item>
    <guid>entry-1</guid>
    <title>Item 1</title>
    <link>https://example.com/item-1</link>
    <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
    <description>Short summary from feed.</description>
  </item>
</channel></rss>
"""
_SINCE = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)


def _multi_feed(count: int) -> str:
    items = "".join(
        f"""
        <item>
          <guid>entry-{index}</guid>
          <title>Item {index}</title>
          <link>https://example.com/item-{index}</link>
          <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
          <description>Summary {index}.</description>
        </item>
        """
        for index in range(1, count + 1)
    )
    return f'<?xml version="1.0"?><rss version="2.0"><channel>{items}</channel></rss>'


def _make_feed_client(feed_text: str) -> AsyncMock:
    response = MagicMock()
    response.text = feed_text
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    return client


def test_rss_ids_are_deterministic() -> None:
    client = _make_feed_client(_FEED)
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)

    first = asyncio.run(scraper.fetch(_SINCE))[0].id
    second = asyncio.run(scraper.fetch(_SINCE))[0].id

    assert first == second
    assert first == "rss:example.com_feed.xml:5e2d5d1e58e94d76"


def _make_registry(name: str, extractor):
    registry = MagicMock()
    registry.get.side_effect = lambda n: extractor if n == name else None
    return registry


def test_content_extractor_replaces_feed_content() -> None:
    client = _make_feed_client(_FEED)
    extractor = AsyncMock()
    extractor.extract.return_value = "Full article text from extractor."

    source = RSSSourceConfig(
        name="Test", url="https://example.com/feed.xml", content_extractor="my-ext"
    )
    scraper = RSSScraper([source], client, extractors=_make_registry("my-ext", extractor))
    items = asyncio.run(scraper.fetch(_SINCE))

    assert len(items) == 1
    assert items[0].content == "Full article text from extractor."
    extractor.extract.assert_awaited_once_with("https://example.com/item-1", client)


def test_content_extractor_falls_back_on_none() -> None:
    client = _make_feed_client(_FEED)
    extractor = AsyncMock()
    extractor.extract.return_value = None  # extraction failed

    source = RSSSourceConfig(
        name="Test", url="https://example.com/feed.xml", content_extractor="my-ext"
    )
    scraper = RSSScraper([source], client, extractors=_make_registry("my-ext", extractor))
    items = asyncio.run(scraper.fetch(_SINCE))

    assert len(items) == 1
    assert items[0].content == "Short summary from feed."


def test_unknown_extractor_name_ignored() -> None:
    client = _make_feed_client(_FEED)
    source = RSSSourceConfig(
        name="Test", url="https://example.com/feed.xml", content_extractor="nonexistent"
    )
    scraper = RSSScraper([source], client, extractors=_make_registry("other", AsyncMock()))
    items = asyncio.run(scraper.fetch(_SINCE))

    assert len(items) == 1
    assert items[0].content == "Short summary from feed."


def test_source_max_items_limits_only_eligible_entries() -> None:
    client = _make_feed_client(_multi_feed(4))
    source = RSSSourceConfig(
        name="High volume",
        url="https://example.com/feed.xml",
        max_items=2,
    )

    items = asyncio.run(RSSScraper([source], client).fetch(_SINCE))

    assert [item.title for item in items] == ["Item 1", "Item 2"]


def test_source_max_items_must_be_positive() -> None:
    with pytest.raises(ValidationError):
        RSSSourceConfig(
            name="Invalid",
            url="https://example.com/feed.xml",
            max_items=0,
        )


def test_transient_rss_failure_retries_then_succeeds(monkeypatch) -> None:
    response = MagicMock()
    response.text = _FEED
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.side_effect = [httpx.ConnectError("temporary"), response]
    sleep = AsyncMock()
    monkeypatch.setattr("src.scrapers.rss.asyncio.sleep", sleep)
    source = RSSSourceConfig(name="Retry", url="https://example.com/feed.xml")

    items = asyncio.run(RSSScraper([source], client).fetch(_SINCE))

    assert len(items) == 1
    assert client.get.await_count == 2
    sleep.assert_awaited_once_with(2)


def test_rss_source_stops_after_three_attempts(monkeypatch) -> None:
    client = AsyncMock()
    client.get.side_effect = httpx.ConnectError("offline")
    sleep = AsyncMock()
    monkeypatch.setattr("src.scrapers.rss.asyncio.sleep", sleep)
    source = RSSSourceConfig(name="Retry", url="https://example.com/feed.xml")

    items = asyncio.run(RSSScraper([source], client).fetch(_SINCE))

    assert items == []
    assert client.get.await_count == 3
    assert [call.args[0] for call in sleep.await_args_list] == [2, 8]
