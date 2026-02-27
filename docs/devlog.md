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

02-24-2026

Worked on:

- Replaced LLM-based decision engine with deterministic SMA crossover strategy.
- Introduced strategy abstraction (BaseStrategy) to make backtest engine strategy-agnostic.
- Refactored backtest logic to separate signal generation from execution.
- Integrated SMA strategy into FastAPI app and verified working UI.

Key lessons:

- Deterministic strategies improve reproducibility and debugging.
- Backtest engine should not depend on specific strategy logic.
- Clear separation of data → strategy → execution improves extensibility.
- External API dependencies complicate development and scalability.

Architecture thoughts:

- Strategy layer now modular and extensible (future ML/LLM integration possible).
- Next step is adding performance metrics and benchmark comparison.
- UI still recomputes backtest on each request — acceptable for now.

Temporary decisions:

- Removed OpenAI integration entirely.
- Using SMA (20/50) as baseline strategy for evaluation.