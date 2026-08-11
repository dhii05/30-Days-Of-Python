# counting investment dividend

# data input
capital_starter = 100000.00 #RM
dividend_yield = 7.8 #7.8%
name_of_stock = "Yari-yari Inc."

# calculation
dividend_amount = capital_starter * (dividend_yield / 100)
total_amount = capital_starter + dividend_amount

# result display
print("*** DIVIDEND STATEMENT ***")
print('investment:', name_of_stock)
print('capital:', capital_starter)
print('dividend rate:', dividend_yield, '%')
print('---------------------')
print('dividend amount:', dividend_amount)
print('total amount of dividend:', total_amount)