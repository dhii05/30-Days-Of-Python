import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")
df["Status"] = np.where(df["Expense"] > 1200, "High", "Normal")

expenses = df["Expense"].to_numpy()

highest_index = np.argmax(expenses)
best_month = df["Month"].iloc[highest_index]

print(df)
print(f"\nTotal: RM{np.sum(expenses):.2f}")
print(f"Average: RM{np.mean(expenses):.2f}")
print(f"Highest: RM{np.max(expenses):.2f}")
print(f"Lowest: RM{np.min(expenses):.2f}")
print(f"Highest Index: {highest_index}")
print(F"Highest Months: {best_month}")

plt.bar(df["Month"],df["Expense"])
plt.title("2026 Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Expenses (RM)")
plt.show()