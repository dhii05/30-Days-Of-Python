# order dictionary
order = {
    'name': 'lily park',
    'list_of_drinks': ['Americano', 'Soda', 'Melon Soda'],
    'price_of_drinks':[8.00, 3.50, 6.50],
    'tax': 1.50
}

# data update
order['name'] = order['name'].title()
order['list_of_drinks'].append('Teh Ais')
order['price_of_drinks'].append(2.50)
order['list_of_drinks'].remove('Soda')
order['price_of_drinks'].remove(3.50)

# calculation
Total_amount_of_drink = sum(order['price_of_drinks'])
Total_amount = Total_amount_of_drink + order.get('tax', 0)

# Receipt
print('---')
print(f'Customer Name: {order.get('name')}')
print(f'List of Drinks: {order.get('list_of_drinks')}')
print(f'Total Amount: RM {Total_amount:,.2f}')
print('---')