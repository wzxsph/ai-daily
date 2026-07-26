#!/usr/bin/env python3
"""Send one bilingual AI Daily email or a short workflow failure alert."""

import argparse
import html
import os
import smtplib
import ssl
import time
from collections.abc import Callable, Sequence
from email.message import EmailMessage
from pathlib import Path


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
RETRY_DELAYS_SECONDS = (5, 20, 60)


def load_credentials() -> tuple[str, str]:
    """Load Gmail credentials by name without ever echoing their values."""
    address = os.getenv("GMAIL_ADDRESS", "").strip()
    password = os.getenv("GMAIL_APP_PASSWORD", "").strip()
    missing = [
        name
        for name, value in (
            ("GMAIL_ADDRESS", address),
            ("GMAIL_APP_PASSWORD", password),
        )
        if not value
    ]
    if missing:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
    return address, password


def _read_summary(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Missing summary file: {path}")
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        raise ValueError(f"Summary file is empty: {path}")
    return content


def build_daily_message(
    date: str,
    address: str,
    summaries_dir: Path,
    pages_url: str,
) -> EmailMessage:
    """Build one multipart email with Chinese first and English second."""
    from markdown import markdown

    zh = _read_summary(summaries_dir / f"horizon-{date}-zh.md")
    en = _read_summary(summaries_dir / f"horizon-{date}-en.md")

    plain = (
        f"AI Daily · {date}\n\n"
        f"中文简报\n{'=' * 8}\n\n{zh}\n\n"
        f"English Briefing\n{'=' * 16}\n\n{en}\n\n"
        f"Pages: {pages_url}\n"
    )
    body_html = (
        "<!doctype html><html><body style=\"font-family:system-ui,-apple-system,sans-serif;"
        "max-width:760px;margin:auto;padding:24px;line-height:1.65;color:#202124\">"
        f"<h1>AI Daily · {html.escape(date)}</h1>"
        "<h2>中文简报</h2>"
        f"{markdown(zh, extensions=['extra'])}"
        "<hr style=\"margin:40px 0\"><h2>English Briefing</h2>"
        f"{markdown(en, extensions=['extra'])}"
        f"<hr><p><a href=\"{html.escape(pages_url, quote=True)}\">查看 AI Daily 历史 / View archive</a></p>"
        "<p style=\"color:#666;font-size:13px\">AI Daily is powered by the MIT-licensed Horizon project.</p>"
        "</body></html>"
    )

    message = EmailMessage()
    message["Subject"] = f"AI Daily | {date} | 中英双语简报"
    message["From"] = address
    message["To"] = address
    message["Message-ID"] = f"<ai-daily-{date}@github-actions>"
    message.set_content(plain)
    message.add_alternative(body_html, subtype="html")
    return message


def build_failure_message(date: str, address: str, run_url: str) -> EmailMessage:
    """Build a concise alert that contains no credentials or captured logs."""
    message = EmailMessage()
    message["Subject"] = f"[FAILED] AI Daily | {date}"
    message["From"] = address
    message["To"] = address
    message["Message-ID"] = f"<ai-daily-failure-{date}@github-actions>"
    message.set_content(
        "AI Daily 的本次自动任务最终失败，未发布未经验证的旧内容。\n\n"
        f"GitHub Actions Run: {run_url}\n"
    )
    message.add_alternative(
        "<p>AI Daily 的本次自动任务最终失败，未发布未经验证的旧内容。</p>"
        f'<p><a href="{html.escape(run_url, quote=True)}">查看 GitHub Actions Run</a></p>',
        subtype="html",
    )
    return message


def send_with_retry(
    message: EmailMessage,
    address: str,
    password: str,
    *,
    retry_delays: Sequence[float] = RETRY_DELAYS_SECONDS,
    smtp_factory: Callable[..., object] = smtplib.SMTP_SSL,
    sleeper: Callable[[float], None] = time.sleep,
) -> None:
    """Send with three independent retries after the initial SMTP attempt."""
    attempts = len(retry_delays) + 1
    last_error: Exception | None = None

    for attempt in range(1, attempts + 1):
        try:
            context = ssl.create_default_context()
            with smtp_factory(SMTP_HOST, SMTP_PORT, context=context, timeout=30) as smtp:
                smtp.login(address, password)
                smtp.send_message(message, from_addr=address, to_addrs=[address])
            print(f"Email sent on SMTP attempt {attempt}/{attempts}")
            return
        except Exception as exc:
            last_error = exc
            if attempt >= attempts:
                break
            delay = retry_delays[attempt - 1]
            print(
                f"SMTP attempt {attempt}/{attempts} failed ({type(exc).__name__}); "
                f"retrying in {delay:g}s",
                flush=True,
            )
            sleeper(delay)

    raise RuntimeError(f"email delivery failed after {attempts} attempts") from last_error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--summaries-dir", type=Path, default=Path("data/summaries"))
    parser.add_argument(
        "--pages-url",
        default="https://wzxsph.github.io/ai-daily/",
    )
    parser.add_argument("--failure", action="store_true")
    parser.add_argument("--run-url", default="")
    args = parser.parse_args()

    address, password = load_credentials()
    if args.failure:
        if not args.run_url:
            raise RuntimeError("--run-url is required for failure alerts")
        message = build_failure_message(args.date, address, args.run_url)
    else:
        message = build_daily_message(
            args.date,
            address,
            args.summaries_dir,
            args.pages_url,
        )
    send_with_retry(message, address, password)


if __name__ == "__main__":
    main()
