# investor dictionary
investor = {
    'name': 'lily park',
    'id': 'NBDSH-544',
    'stock_list': ['MY', 'CB', 'TG'],
    'stock_value': [600.00, 500.00, 680.00],
    'balance': 800.00
}

# data update
investor['name'] = investor['name'].title()
investor['stock_list'].append('TNB')
investor['stock_value'].append(800.00)
investor['stock_list'].remove('TG')
investor['stock_value'].remove(680.00)

# calculation
total_stock_value = sum(investor['stock_value'])
total_amount_of_portfolio = total_stock_value + investor.get('balance',0)

# receipt
print('---')
print(f'investor name: {investor.get('name')}')
print(f'investor ID: {investor.get('id')}')
print(f'List of Share: {investor.get('stock_list')}')
print(f'Total Share: {total_stock_value:,.2f}')
print(f'total portfolio: RM {total_amount_of_portfolio:,.2f}')
print('---')