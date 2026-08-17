# input
monthly_income = float(input('Monthly Income '))
annual_income = monthly_income * 12
taxable_income = annual_income

# zakat
def zakat_calculation(annual_income, nisab=42047):
    if annual_income >= nisab:
        zakat = annual_income * 2.5 / 100
        eligible = True
    else:
        zakat = 0.0
        eligible = False
    return zakat, eligible

# tax
def tax_calculation(taxable_income):
    tax = 0.0
    if taxable_income <= 5000:
        tax = 0.00
    elif taxable_income <= 20000:
        tax = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax = ((20000 - 5000) * 0.01) + (taxable_income - 20000) * 0.03
    else:
        tax = ((20000 - 5000) * 0.01) + ((35000 - 20000) * 0.03) + (taxable_income - 35000) * 0.08
    return tax

zakat, eligible = zakat_calculation(annual_income)
total_gross_tax = tax_calculation(taxable_income)
total_net_tax = max(0.0, total_gross_tax - zakat)

print('\n' + '=' * 40)
print(' summary of zakat and annual tax')
print('=' * 40)
print(f'Monthly Income: RM {monthly_income:,.2f}')
print(f'Annual Income: RM {annual_income:,.2f}')
print('-' * 40)

if eligible:
    print(f'Zakat Status: eligible (Wajib)')
    print(f'Total Zakat (2.5%): RM {zakat:,.2f}')
else:
    print(f'Zakat Status: not eligible (Under Nisab)')
    print(f'Total Zakat: RM 0.00')

print('-' * 40)
print(f'Gross Tax: RM {total_gross_tax:,.2f}')
print(f'Rebate Zakat: RM {zakat:,.2f}')
print(f'Net Tax that will be Charged: RM {total_net_tax:,.2f}')
print('-' * 40)