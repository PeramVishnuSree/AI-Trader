from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from strategies.sma import SMACrossoverStrategy
import pandas as pd

from data.data_loader import get_price_history
from backtest.engine import run_backtest

app = FastAPI()
templates = Jinja2Templates(directory = "dashboard/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    data = get_price_history("AAPL", "2022-01-01", "2023-01-01")
    strategy = SMACrossoverStrategy(short_window=20, long_window=50)
    results = run_backtest(data, strategy)

    final_value = results.iloc[-1]["portfolio_value"]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "final_value": round(final_value, 2),
            "rows": results.tail(20).to_dict(orient="records")
        }
    )
