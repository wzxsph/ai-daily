"""Run-date helpers shared by the daily pipeline and notifications."""

import os
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


DEFAULT_TIMEZONE = "UTC"


def configured_timezone() -> ZoneInfo:
    """Resolve the reporting timezone without relying on runner-local settings."""
    timezone_name = os.getenv("HORIZON_TIMEZONE", DEFAULT_TIMEZONE).strip()
    try:
        return ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as exc:
        raise ValueError(f"Unknown HORIZON_TIMEZONE: {timezone_name}") from exc


def current_run_date(now: datetime | None = None) -> str:
    """Return the calendar date used for output filenames."""
    timezone = configured_timezone()
    instant = now or datetime.now(tz=timezone)
    if instant.tzinfo is None:
        raise ValueError("current_run_date requires a timezone-aware datetime")
    return instant.astimezone(timezone).strftime("%Y-%m-%d")
