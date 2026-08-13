# creating investor profile
investor = {
    'name': 'Lily',
    'age': 22,
    'profile_risk': 'medium',
    'capital': 450000.00,
    'status_activation': True
}

# access data using key value
print(investor['name'])
print(investor.get('profile_risk')) #this is more safe if the key isn't there

# updating the key value
investor['capital'] = 70000.00

# adding new key value 
investor['location'] = 'Kuala_Lumpur'

# discard a key value
investor.pop('status_activation')

investor_profile = {
    'investor_id': 'JJDN-55145',
    'name': 'Lily',
    'risk': 'high',
    'stock_portfolio': ['Yari_Yari', 'Poli', 'Yang'],
    'total_amount': 50000.00
}

# access item in list in dictionary
main_share = investor_profile['stock_portfolio'][0]
print(f'main share {investor_profile[ 'name' ]} is {main_share}.')