import numpy as np

months = ["Jan", "Feb", "March", "Apr", "May"]

savings = np.array([300, 450, 250, 500, 400])

for month, saving in zip(months, savings):
    print(f"{month}: RM{saving:.2f}")

print(f"\nTotal: RM{np.sum(savings):.2f}")
print(f"Average: RM{np.mean(savings):.2f}")
print(f"Highest: RM{np.max(savings):.2f}")
print(f"Lowest: RM{np.min(savings):.2f}")