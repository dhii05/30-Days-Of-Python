import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tnb = yf.download(
    "5347.KL",
    start="2025-01-01",
    end="2025-12-31"
)
tnb["SMA_5"] = tnb["Close"].rolling(window=5).mean()
tnb["EMA_5"] = tnb["Close"].ewm(
    span=5,
    adjust=False
).mean()

print(tnb[["Close", "SMA_5", "EMA_5"]].tail(10))

plt.plot(tnb.index, tnb["Close"], label="Close")
plt.plot(tnb.index, tnb["SMA_5"], label="SMA 5")
plt.plot(tnb.index, tnb["EMA_5"], label="EMA 5")

plt.title("TNB Moving Averages (2025)")
plt.xlabel("Date")
plt.ylabel("Price (RM)")
plt.legend()
plt.grid(True)
plt.show()