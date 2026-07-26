#!/usr/bin/env python3
"""Run the complete daily pipeline twice at most, validating each attempt."""

import argparse
import subprocess
import sys
import time
from collections.abc import Callable, Sequence
from pathlib import Path

from src.output_validation import output_paths, validate_daily_output


def clear_daily_outputs(
    date: str,
    summaries_dir: Path = Path("data/summaries"),
    posts_dir: Path = Path("docs/_posts"),
) -> None:
    """Remove only the current run's known targets to prevent mixed attempts."""
    for path in output_paths(date, summaries_dir, posts_dir):
        path.unlink(missing_ok=True)


def run_with_retry(
    command: Sequence[str],
    date: str,
    *,
    attempts: int = 2,
    retry_delay: float = 120,
    runner: Callable[..., subprocess.CompletedProcess] = subprocess.run,
    validator: Callable[[str], object] = validate_daily_output,
    sleeper: Callable[[float], None] = time.sleep,
) -> None:
    """Run a command and validation gate, retrying the whole unit on failure."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        clear_daily_outputs(date)
        print(f"Starting daily pipeline attempt {attempt}/{attempts}", flush=True)
        try:
            result = runner(list(command), check=False)
            if result.returncode != 0:
                raise RuntimeError(f"pipeline exited with status {result.returncode}")
            validator(date)
            print(f"Daily pipeline attempt {attempt} passed validation", flush=True)
            return
        except Exception as exc:
            last_error = exc
            if attempt >= attempts:
                break
            print(
                f"Daily pipeline attempt {attempt} failed ({type(exc).__name__}); "
                f"retrying in {retry_delay:g}s",
                flush=True,
            )
            sleeper(retry_delay)

    raise RuntimeError(f"daily pipeline failed after {attempts} attempts") from last_error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hours", type=int, required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--attempts", type=int, default=2)
    parser.add_argument("--retry-delay", type=float, default=120)
    args = parser.parse_args()

    command = [sys.executable, "-m", "src.main", "--hours", str(args.hours)]
    run_with_retry(
        command,
        args.date,
        attempts=args.attempts,
        retry_delay=args.retry_delay,
    )


if __name__ == "__main__":
    main()
