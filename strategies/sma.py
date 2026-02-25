import pandas as pd
from strategies.base import BaseStrategy

class SMACrossoverStrategy(BaseStrategy):

    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signal(self, data: pd.DataFrame) -> str:
        
        if len(data) < self.long_window:
            return "HOLD"
        
        short_sma = data["Close"].rolling(self.short_window).mean().iloc[-1]
        long_sma = data["Close"].rolling(self.long_window).mean().iloc[-1]

        if short_sma > long_sma:
            return "BUY"
        elif short_sma < long_sma:
            return "SELL"
        else:
            return "HOLD"