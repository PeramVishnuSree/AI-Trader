import yfinance as yf
import pandas as pd

def get_price_history(symbol: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(symbol, start=start, end=end)

    #Handle multi index columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df[["Close"]]
    df.dropna(inplace=True)
    
    return df