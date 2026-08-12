# compound interest calculation

# data input
principal = 5000.00
rate = 0.6
compound = 4
time = 7

# compound interest calculation
amount = principal * ( 1 + rate / compound) ** (compound * time)
profit = amount - principal

# result display
print('*** Compound Interest Statement (7 years) ***')
print('Principal: RM', principal)
print('Rate of Return:', rate * 100, '%')
print('Tenure:', time, 'year')
print('-----------------')
print('Profit of Interest: RM', round(profit, 2))
print('Total Amount: RM', round(amount, 2))
