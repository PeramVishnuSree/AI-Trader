import os
from openai import OpenAI
from dotenv import load_dotenv
import random

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def summarize_market(data):
    last_price = float(data.iloc[-1]["Close"])
    avg_price = float(data["Close"].mean())
    change = (last_price - avg_price) / avg_price *100

    # print(type(data))
    # print(data.columns)
    # print(data.head())

    return f""" 
            Last Price: {last_price:.2f}
            Average Price: {avg_price:.2f}
            % Change vs Aug: {change:.2f}%
            """ 

def get_decision(summary: str):
    # prompt = f"""
    # You are a trading agent.
    # Based on this market summary:

    # {summary}

    # Respond ONLY with one word:
    # BUY, SELL, or HOLD.
    # """

    # response = client.chat.completions.create(
    #     model = "gpt-4.1-mini",
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=0
    # )

    # decision = response.choices[0].message.content.strip().upper()

    # if decision not in ["BUY", "SELL", "HOLD"]:
    #     return "HOLD"
    
    
    return random.choice(["BUY", "SELL", "HOLD"])