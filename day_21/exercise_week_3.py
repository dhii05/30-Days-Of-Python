import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

today = datetime.now()
df = pd.read_csv("savings.csv")

print(df.isnull().sum())

df["Savings"] = df["Savings"].fillna(df["Savings"].mean())
savings = np.array(df["Savings"])

print(df)
print(f"\nTotal: RM{np.sum(savings):.2f}")
print(f"Average: RM{np.mean(savings):.2f}")
print(f"Highest: RM{np.max(savings):.2f}")
print(f"Lowest: RM{np.min(savings):.2f}")
print(f"Analysis Date: {today.strftime('%d %m %Y')}")
plt.bar(df["Months"],df["Savings"])
plt.title("2026 Monthly Savings")
plt.xlabel("Months")
plt.ylabel("Savings (RM)")
plt.show()