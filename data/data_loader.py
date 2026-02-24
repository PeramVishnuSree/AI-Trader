import yfinance as yf
import pandas as pd

def get_price_history(symbol: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(symbol, start=start, end=end)
    df = df[['Close']]
    df.dropna(inplace=True)
    return df