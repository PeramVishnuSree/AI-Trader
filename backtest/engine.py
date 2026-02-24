import pandas as pd
from agents.llm_agent import summarize_market, get_decision

def run_backtest(data: pd.DataFrame, initial_cash = 10000):
    cash = initial_cash
    shares = 0
    history = []

    for i in range(30, len(data)): # because we need 30 days of history
        window = data.iloc[i-30: i]
        price = data.iloc[i]["Close"]

        summary = summarize_market(window)
        decision = get_decision(summary)

        if decision == "BUY" and cash > price:
            shares = cash // price
            cash -= price*shares

        elif decision == "SELL" and shares > 0:
            cash += shares * price
            shares = 0

        portfolio_value = cash + shares * price

        history.append({
            "date": data.index[i],
            "decision": decision,
            "portfolio_value": portfolio_value
        })

    return pd.DataFrame(history)