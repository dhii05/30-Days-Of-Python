import math
print(math.sqrt(144))
print(math.floor(8.7))

from datetime import datetime
today = datetime.now()
start = datetime(2026, 8, 24)
end = datetime(2026, 9, 5)

difference = end - start

print(today.strftime("%d %B %Y"))
print(today.strftime("%I:%M %p"))
print(difference.days)

money_save = float(input("Saved "))

print(f"Saved {money_save:.2f} on {today.strftime('%d/%m/%Y')} {today.strftime('%I:%M %p')}")