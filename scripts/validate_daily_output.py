#!/usr/bin/env python3
"""CLI validation gate used immediately before Pages deployment."""

import argparse
from pathlib import Path

from src.output_validation import validate_daily_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--summaries-dir", type=Path, default=Path("data/summaries"))
    parser.add_argument("--posts-dir", type=Path, default=Path("docs/_posts"))
    parser.add_argument("--max-items", type=int, default=15)
    args = parser.parse_args()

    result = validate_daily_output(
        args.date,
        summaries_dir=args.summaries_dir,
        posts_dir=args.posts_dir,
        max_items=args.max_items,
    )
    print(f"Validated {len(result.files)} files with {result.item_count} bilingual items")


if __name__ == "__main__":
    main()
