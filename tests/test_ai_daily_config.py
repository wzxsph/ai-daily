import json
from datetime import datetime, timezone
from pathlib import Path

from src.models import AIProvider, Config
from src.time_utils import current_run_date


def test_production_config_matches_ai_daily_contract() -> None:
    payload = json.loads(Path("data/config.github.json").read_text(encoding="utf-8"))
    config = Config.model_validate(payload)

    assert config.ai.provider == AIProvider.MINIMAX
    assert config.ai.model == "MiniMax-M3"
    assert config.ai.base_url == "https://api.minimaxi.com/anthropic"
    assert config.ai.api_key_env == "MINIMAX_API_KEY"
    assert config.ai.max_tokens == 8192
    assert config.ai.languages == ["zh", "en"]
    assert config.ai.analysis_concurrency == 3
    assert config.ai.enrichment_concurrency == 2

    filtering = config.filtering
    assert filtering.ai_score_threshold == 7.5
    assert filtering.max_items == 15
    assert {key: group.limit for key, group in filtering.category_groups.items()} == {
        "models_products": 4,
        "agents_tools": 4,
        "github_trends": 3,
        "research": 2,
        "industry_policy": 2,
    }

    arxiv = [source for source in config.sources.rss if source.name.startswith("arXiv")]
    assert len(arxiv) == 3
    assert all(source.max_items == 5 for source in arxiv)
    assert config.sources.telegram.enabled is False
    assert config.sources.twitter and config.sources.twitter.enabled is False
    assert config.sources.openbb and config.sources.openbb.enabled is False
    assert config.sources.gdelt and config.sources.gdelt.enabled is False
    assert config.sources.google_news and config.sources.google_news.enabled is False
    assert config.email is None


def test_beijing_run_date_uses_next_calendar_day(monkeypatch) -> None:
    monkeypatch.setenv("HORIZON_TIMEZONE", "Asia/Shanghai")
    late_utc = datetime(2026, 7, 26, 23, 30, tzinfo=timezone.utc)

    assert current_run_date(late_utc) == "2026-07-27"
