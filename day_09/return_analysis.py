# input

saving = float(input('Saving: '))
dividend_rate = float(input('Dividend: ')) / 100
tenure = int(input('Year: '))

for tenure in range(1, tenure + 1):
    dividend = saving * dividend_rate
    saving = saving + dividend
    print(f'Year {tenure}: Dividend = RM {dividend:,.2f} | Current Saving = RM {saving:,.2f}')