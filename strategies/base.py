from abc import ABC, abstractmethod
import pandas as pd

class BaseStrategy(ABC):

    @abstractmethod
    def generate_signal(self, data: pd.DataFrame) -> str:
        """
        Given historical price data,
        return 'BUY', 'SELL', or 'HOLD'
        """
        pass