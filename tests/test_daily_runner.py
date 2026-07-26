import subprocess
from pathlib import Path

import pytest

from scripts.run_daily_with_retry import run_with_retry
from src.output_validation import validate_daily_output


def _write_valid_outputs(root: Path, date: str) -> None:
    content = '<a id="item-1"></a>\n## [Item](https://example.com/original)'
    for directory in (root / "data/summaries", root / "docs/_posts"):
        directory.mkdir(parents=True, exist_ok=True)
    for language in ("zh", "en"):
        (root / "data/summaries" / f"horizon-{date}-{language}.md").write_text(
            content, encoding="utf-8"
        )
        (root / "docs/_posts" / f"{date}-summary-{language}.md").write_text(
            content, encoding="utf-8"
        )


def test_complete_pipeline_retries_then_validates(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    calls = 0
    sleeps: list[float] = []

    def runner(command, check):
        nonlocal calls
        calls += 1
        if calls == 2:
            _write_valid_outputs(tmp_path, "2026-07-27")
            return subprocess.CompletedProcess(command, 0)
        return subprocess.CompletedProcess(command, 1)

    run_with_retry(
        ["horizon"],
        "2026-07-27",
        runner=runner,
        validator=validate_daily_output,
        sleeper=sleeps.append,
    )

    assert calls == 2
    assert sleeps == [120]


def test_complete_pipeline_final_failure_is_not_silent(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)

    def runner(command, check):
        return subprocess.CompletedProcess(command, 1)

    with pytest.raises(RuntimeError, match="failed after 2 attempts"):
        run_with_retry(
            ["horizon"],
            "2026-07-27",
            runner=runner,
            sleeper=lambda _: None,
        )
