# Dev Log

02-23-2026

Worked on:
- Built basic architecture: data -> strategy -> backtest -> FastAPI UI.
- Introduced config layer for environment-based settings
- Fixed pandas MultiIndex issue from yfinance response.

Key lessons:
- Assumptions about data shape breaks logic.
- Calling LLM inside backtesting loop is expensive and not scalable.
- UI route should not recompute havy logic on each request.

Architecture thoughts:
- Need caching layer or decouple computer from render
- Eventually need metrics layer (Sharpe, drawdown).
- LLM intergration must be controled and minimized.

Temporary decisions:
- Replaced LLM decision engine with random strategy for now. 