import pandas as pd
# from agents.llm_agent import summarize_market, get_decision
from core.config import Settings

def run_backtest(data: pd.DataFrame, strategy):
    cash = Settings.INITAL_CASH
    shares = 0
    history = []

    for i in range(len(data)):
        window = data.iloc[:i+1]
        price = data.iloc[i]["Close"]

        signal = strategy.iloc[i]["Close"]

        if signal == "BUY" and cash > price:
            shares_to_buy = int(cash // price)
            cash -= shares_to_buy * price
            shares += shares_to_buy

        elif signal == "SELL" and shares > 0:
            cash += shares * price
            shares = 0

        portfolio_value = cash + shares * price

        history.append({
            "date": str(data.index[i].date()),
            "signal": signal,
            "cash": round(cash, 2),
            "shares": shares,
            "portfolio_value": round(portfolio_value, 2),
            "price": round(price, 2)
        })

    return pd.DataFrame(history)