import pandas as pd

data = {
    "Date": ["18 Aug", "19 Aug", "20 Aug", "21 Aug", "22 Aug"],
    "Price": [9.82, 9.91, 9.88, 10.02, 9.97]
}
df = pd.DataFrame(data)

print(df)
print(df["Price"].mean())
print(df["Price"].max())
print(df["Price"].min())

# example from gpt
import pandas as pd

data = {
    "Date": ["18 Aug", "19 Aug", "20 Aug", "21 Aug", "22 Aug"],
    "Price": [9.82, 9.91, 9.88, 10.02, 9.97]
}

df = pd.DataFrame(data)

print("\n=== MAYBANK SHARE PRICE ===")
print(df)

print(f"\nAverage Price : RM{df['Price'].mean():.2f}")
print(f"Highest Price : RM{df['Price'].max():.2f}")
print(f"Lowest Price  : RM{df['Price'].min():.2f}")