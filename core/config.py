import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DEFAULT_SYMBOL = "AAPL"
    INITAL_CASH = 10000