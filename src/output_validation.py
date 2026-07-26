"""Validation gates for generated bilingual daily output."""

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


LANGUAGES = ("zh", "en")
PLACEHOLDER_MARKERS = (
    "no significant developments today",
    "none met the importance threshold",
    "今日暂无重要动态",
    "没有达到重要性阈值",
)
HTTP_LINK_PATTERN = re.compile(r"https?://[^\s)>\]]+", re.IGNORECASE)
ITEM_PATTERN = re.compile(r'<a id="item-(\d+)"></a>')
ITEM_HEADING_LINK_PATTERN = re.compile(r"(?m)^## .*https?://")


class OutputValidationError(ValueError):
    """Raised when generated content is unsafe to publish."""


@dataclass(frozen=True)
class ValidationResult:
    """Validated output metadata."""

    date: str
    item_count: int
    files: tuple[Path, ...]


def validate_date(value: str) -> str:
    """Require a canonical ISO calendar date before constructing paths."""
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise OutputValidationError(f"Invalid date: {value!r}") from exc
    if parsed.strftime("%Y-%m-%d") != value:
        raise OutputValidationError(f"Invalid date: {value!r}")
    return value


def output_paths(
    date: str,
    summaries_dir: Path = Path("data/summaries"),
    posts_dir: Path = Path("docs/_posts"),
) -> tuple[Path, ...]:
    """Return the four files that must be complete before deployment."""
    date = validate_date(date)
    return tuple(
        path
        for language in LANGUAGES
        for path in (
            summaries_dir / f"horizon-{date}-{language}.md",
            posts_dir / f"{date}-summary-{language}.md",
        )
    )


def validate_daily_output(
    date: str,
    summaries_dir: Path = Path("data/summaries"),
    posts_dir: Path = Path("docs/_posts"),
    max_items: int = 15,
) -> ValidationResult:
    """Reject missing, empty, placeholder, linkless, or oversized output."""
    files = output_paths(date, summaries_dir, posts_dir)
    item_counts: dict[str, int] = {}

    for path in files:
        if not path.is_file():
            raise OutputValidationError(f"Missing generated file: {path}")
        content = path.read_text(encoding="utf-8").strip()
        if not content:
            raise OutputValidationError(f"Generated file is empty: {path}")

        lowered = content.casefold()
        if any(marker in lowered for marker in PLACEHOLDER_MARKERS):
            raise OutputValidationError(f"Placeholder summary cannot be published: {path}")
        if not HTTP_LINK_PATTERN.search(content):
            raise OutputValidationError(f"Generated file has no original link: {path}")

        item_ids = ITEM_PATTERN.findall(content)
        if not item_ids:
            raise OutputValidationError(f"Generated file has no digest items: {path}")
        if len(item_ids) > max_items:
            raise OutputValidationError(
                f"Generated file exceeds {max_items} items ({len(item_ids)}): {path}"
            )

        item_blocks = ITEM_PATTERN.split(content)[2::2]
        if any(not ITEM_HEADING_LINK_PATTERN.search(block) for block in item_blocks):
            raise OutputValidationError(
                f"Every digest item must link its original source: {path}"
            )

        language = path.stem.rsplit("-", 1)[-1]
        existing = item_counts.setdefault(language, len(item_ids))
        if existing != len(item_ids):
            raise OutputValidationError(
                f"Summary and Pages copy disagree for {language}: {path}"
            )

    if item_counts.get("zh") != item_counts.get("en"):
        raise OutputValidationError(
            "Chinese and English summaries contain different item counts"
        )

    return ValidationResult(date=date, item_count=item_counts["zh"], files=files)
