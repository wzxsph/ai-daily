from pathlib import Path

import pytest

from scripts.send_daily_email import (
    build_daily_message,
    load_credentials,
    send_with_retry,
)


class FakeSMTP:
    def __init__(self) -> None:
        self.login_args = None
        self.message = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def login(self, address, password) -> None:
        self.login_args = (address, password)

    def send_message(self, message, **kwargs) -> None:
        self.message = message


def _summaries(tmp_path: Path) -> Path:
    directory = tmp_path / "summaries"
    directory.mkdir()
    (directory / "horizon-2026-07-27-zh.md").write_text(
        "# 中文简报\n\n[中文原文](https://example.com/zh)", encoding="utf-8"
    )
    (directory / "horizon-2026-07-27-en.md").write_text(
        "# English Briefing\n\n[Original](https://example.com/en)", encoding="utf-8"
    )
    return directory


def test_missing_gmail_secrets_fails_without_values(monkeypatch) -> None:
    monkeypatch.delenv("GMAIL_ADDRESS", raising=False)
    monkeypatch.delenv("GMAIL_APP_PASSWORD", raising=False)

    with pytest.raises(RuntimeError) as exc:
        load_credentials()

    assert "GMAIL_ADDRESS" in str(exc.value)
    assert "GMAIL_APP_PASSWORD" in str(exc.value)


def test_daily_message_combines_chinese_before_english(tmp_path) -> None:
    message = build_daily_message(
        "2026-07-27",
        "owner@example.com",
        _summaries(tmp_path),
        "https://wzxsph.github.io/ai-daily/",
    )

    plain = message.get_body(preferencelist=("plain",)).get_content()
    html = message.get_body(preferencelist=("html",)).get_content()
    assert plain.index("中文简报") < plain.index("English Briefing")
    assert html.index("中文简报") < html.index("English Briefing")
    assert message["From"] == message["To"] == "owner@example.com"
    assert "https://wzxsph.github.io/ai-daily/" in html


def test_email_retries_after_transient_failure(tmp_path) -> None:
    message = build_daily_message(
        "2026-07-27", "owner@example.com", _summaries(tmp_path), "https://example.com"
    )
    smtp = FakeSMTP()
    calls = 0
    sleeps: list[float] = []

    def factory(*args, **kwargs):
        nonlocal calls
        calls += 1
        if calls == 1:
            raise OSError("temporary")
        return smtp

    send_with_retry(
        message,
        "owner@example.com",
        "app-password",
        smtp_factory=factory,
        sleeper=sleeps.append,
    )

    assert calls == 2
    assert sleeps == [5]
    assert smtp.message is message


def test_email_exhausts_initial_attempt_plus_three_retries(tmp_path) -> None:
    message = build_daily_message(
        "2026-07-27", "owner@example.com", _summaries(tmp_path), "https://example.com"
    )
    calls = 0

    def factory(*args, **kwargs):
        nonlocal calls
        calls += 1
        raise OSError("offline")

    with pytest.raises(RuntimeError, match="after 4 attempts"):
        send_with_retry(
            message,
            "owner@example.com",
            "app-password",
            retry_delays=(0, 0, 0),
            smtp_factory=factory,
            sleeper=lambda _: None,
        )

    assert calls == 4
