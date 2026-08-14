# first concept

# if: for first option
# elif: for next option if before option is false
# else: last option if other option false

# == (equal to)
# != (not equal to)
# > (more than)
# < (less than)
# >= (more than or equal to)
# <= (less than or equal to)

# input
salary = float(input('Your Salary? '))
age = int(input('Your Age? '))
total_monthly_loan = float(input('Your total monthly loan? '))

# calculation
DSR = (total_monthly_loan/salary) * 100
print(f'Your DSR percentage is: {DSR:.2f}')

# requirement approval
if DSR <= 60 and age >= 21:
    print('Loan is approved')
elif DSR > 60: 
    print('Loan disapproved: Your loan credit is too high')
else:
    print('Loan disapproved: Your age doesn\'t following the minimum requirement')