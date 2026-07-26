from pathlib import Path


def test_daily_workflow_preserves_generation_deploy_email_order() -> None:
    workflow = Path(".github/workflows/daily-summary.yml").read_text(encoding="utf-8")

    assert 'cron: "30 23 * * *"' in workflow
    assert "timeout-minutes: 60" in workflow
    assert "lookback_hours:" in workflow
    assert "send_email:" in workflow
    assert "retry-delay 120" in workflow
    assert workflow.count("uses: peaceiris/actions-gh-pages@v4") == 2
    assert "run: sleep 30" in workflow
    assert "steps.deploy_primary.outcome == 'failure'" in workflow

    generate = workflow.index("Generate and validate bilingual briefing")
    deploy = workflow.index("Deploy to GitHub Pages")
    email = workflow.index("Send one bilingual Gmail message")
    assert generate < deploy < email


def test_daily_workflow_uses_only_secret_names_not_values() -> None:
    workflow = Path(".github/workflows/daily-summary.yml").read_text(encoding="utf-8")

    for secret_name in (
        "MINIMAX_API_KEY",
        "GMAIL_ADDRESS",
        "GMAIL_APP_PASSWORD",
    ):
        assert f"secrets.{secret_name}" in workflow
    assert "smtp.gmail.com" not in workflow
    assert "CNAME" not in workflow
