import csv
from datetime import datetime

today = datetime.now()
money_save = float(input("Money Saved: "))

with open ("transaction.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        today.strftime("%d/%m/%Y"),
        today.strftime("%I:%M %p"),
        money_save
    ])

print(f"\nSaved RM {money_save:.2f}")

with open("transaction.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Date: {row[0]}")
        print(f"Time: {row[1]}")
        print(f"Saved: RM {float(row[2]):.2f}")
        print()