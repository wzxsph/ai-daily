# AI Daily Operations

This fork keeps Horizon's MIT license and upstream attribution. Production is intentionally file-only: generated Markdown is published to `gh-pages`; no database, IMAP subscriber list, custom domain, X, Telegram, GDELT, Google News, or OpenBB integration is enabled.

## Required GitHub Actions secrets

Add these in **Settings → Secrets and variables → Actions**. Never put their values in an issue, workflow input, config file, Actions log, or commit.

- `MINIMAX_API_KEY`
- `GMAIL_ADDRESS`
- `GMAIL_APP_PASSWORD`

`GMAIL_APP_PASSWORD` must be a Google app password for the same mailbox named by `GMAIL_ADDRESS`. The workflow sends from and to that one address through `smtp.gmail.com:465`; Horizon's IMAP subscription mechanism remains disabled.

## First-run acceptance

1. Open **Actions → AI Daily Briefing → Run workflow**.
2. Use `lookback_hours = 48` and leave `send_email = false`.
3. Verify the run is green, both languages appear on <https://wzxsph.github.io/ai-daily/>, each item links to an original source, and no more than 15 items were published.
4. Run again with `lookback_hours = 24` and `send_email = true`.
5. Verify exactly one multipart email arrives with Chinese first and English second.

The regular schedule is `30 23 * * *` (07:30 Asia/Shanghai). Scheduled runs always use a 24-hour window and send email after a successful Pages deployment.

## Failure behavior

- HTTP connection retries: 2 at the transport layer.
- RSS: at most 3 attempts per source, with 2- and 8-second waits between attempts.
- AI analysis/enrichment: Horizon's existing 3-attempt exponential retry.
- Complete generation plus validation: 2 attempts, 120 seconds apart.
- Pages: 2 attempts, 30 seconds apart.
- Gmail: initial attempt plus 3 retries after 5, 20, and 60 seconds.

Missing, empty, placeholder, linkless, mismatched, or oversized output fails validation before deployment. Email runs only after Pages succeeds. A final failure attempts a short alert containing the Actions run URL, and the workflow remains red even if that alert cannot be sent.

## Monthly upstream sync

Updates are deliberately manual and reviewed before production:

```bash
git fetch upstream
git switch main
git pull --ff-only origin main
git switch -c sync/horizon-YYYY-MM
git merge --no-ff upstream/main
uv sync --frozen --extra dev
uv run pytest
git push -u origin sync/horizon-YYYY-MM
```

Open a pull request, inspect conflicts in production config/workflows, let tests pass, and merge through the PR. Do not auto-merge `upstream/main` into production.
