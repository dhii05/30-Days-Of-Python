import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tnb = yf.download("5347.KL", start="2025-01-01", end="2025-12-31")

close_price = tnb["Close"]

print(tnb.head())
print(f"Highest: RM{close_price.max():.2f}")
print(f"Lowest : RM{close_price.min():.2f}")
print(f"Average: RM{close_price.mean():.2f}")

plt.plot(tnb.index, tnb["Close"])
plt.title("TNB Closing Price (2025)")
plt.xlabel("Date")
plt.ylabel("Price (RM)")
plt.grid(True)
plt.show()