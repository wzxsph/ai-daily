from pathlib import Path

import pytest

from src.output_validation import OutputValidationError, validate_daily_output


def _content(item_count: int = 2) -> str:
    return "\n\n".join(
        f'<a id="item-{index}"></a>\n## [Item {index}](https://example.com/{index})'
        for index in range(1, item_count + 1)
    )


def _write_outputs(root: Path, date: str, content: str) -> tuple[Path, Path]:
    summaries = root / "summaries"
    posts = root / "posts"
    summaries.mkdir()
    posts.mkdir()
    for language in ("zh", "en"):
        (summaries / f"horizon-{date}-{language}.md").write_text(content, encoding="utf-8")
        (posts / f"{date}-summary-{language}.md").write_text(content, encoding="utf-8")
    return summaries, posts


def test_valid_bilingual_output_passes(tmp_path) -> None:
    summaries, posts = _write_outputs(tmp_path, "2026-07-27", _content())

    result = validate_daily_output(
        "2026-07-27", summaries_dir=summaries, posts_dir=posts
    )

    assert result.item_count == 2
    assert len(result.files) == 4


def test_missing_language_file_fails(tmp_path) -> None:
    summaries, posts = _write_outputs(tmp_path, "2026-07-27", _content())
    (posts / "2026-07-27-summary-en.md").unlink()

    with pytest.raises(OutputValidationError, match="Missing generated file"):
        validate_daily_output("2026-07-27", summaries_dir=summaries, posts_dir=posts)


@pytest.mark.parametrize(
    "content",
    [
        "今日暂无重要动态 https://example.com",
        "No significant developments today https://example.com",
        '<a id="item-1"></a>\nNo original link',
    ],
)
def test_placeholder_or_linkless_output_fails(tmp_path, content) -> None:
    summaries, posts = _write_outputs(tmp_path, "2026-07-27", content)

    with pytest.raises(OutputValidationError):
        validate_daily_output("2026-07-27", summaries_dir=summaries, posts_dir=posts)


def test_more_than_fifteen_items_fails(tmp_path) -> None:
    summaries, posts = _write_outputs(tmp_path, "2026-07-27", _content(16))

    with pytest.raises(OutputValidationError, match="exceeds 15 items"):
        validate_daily_output("2026-07-27", summaries_dir=summaries, posts_dir=posts)


def test_each_item_heading_must_have_its_own_original_link(tmp_path) -> None:
    content = (
        '<a id="item-1"></a>\n## [Linked](https://example.com/1)\n\n'
        '<a id="item-2"></a>\n## Unlinked item'
    )
    summaries, posts = _write_outputs(tmp_path, "2026-07-27", content)

    with pytest.raises(OutputValidationError, match="Every digest item"):
        validate_daily_output("2026-07-27", summaries_dir=summaries, posts_dir=posts)
