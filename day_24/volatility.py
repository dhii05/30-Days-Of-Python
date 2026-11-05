import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = "5341.KL"
data = yf.download(
    ticker,
    period="1y",
    auto_adjust=True
)


data["Daily_Return"] = data["Close"].pct_change() * 100

print(data[["Close", "Daily_Return"]].head(10))


volatility = data["Daily_Return"].std()

print(f"Daily Volatility: {volatility:.2f}%")