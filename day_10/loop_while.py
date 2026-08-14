#input
house_deposit_target = float(input('House Deposit: '))
current_saving = 0
monthly_saving = float(input('Monthly Saving: '))
month = 0

#calculation
while current_saving < house_deposit_target:
    month = month + 1
    current_saving = current_saving + monthly_saving
    print(f'Month: {month}: Saving = RM {current_saving:,.2f}')

print(f'Congrats!\n You reach your house deposit target RM {house_deposit_target:,.2f} in {month} months.')
