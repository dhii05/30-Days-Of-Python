import pandas as pd
import matplotlib.pyplot as plt

data = {
    "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "savings": [300, 450, 250, 500, 400, 550]
}

df = pd.DataFrame(data)

plt.bar(df["months"],df["savings"])
plt.title("2026 Monthly Savings")
plt.xlabel("Months")
plt.ylabel("Savings (RM)")
plt.show()