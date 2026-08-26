import pandas as pd
import numpy as np

data = {
    "Company": ["TNB", "MAYBANK", "maybank", "CIMB", "CIMB"],
    "Price": [14.20, 9.82, 9.82, None, 6.75]
}

df = pd.DataFrame(data)
df["Company"] = df["Company"].str.title()
df["Price"] = df["Price"].fillna(df["Price"].mean())
df = df.drop_duplicates()

print(df)
print(f'Mean: RM {df["Price"].mean():.2f}')