# transaction data
customer_name = 'Lily'
transaction_id = 'BFH-552525-5558'
amount = 5000.00
status = 'succesful'
date_time = '5 Nov 2026, 21:05'

# Notification message
transaction_message = f'''[TRANSACTION RECEIPT]
Hi {customer_name.title()},

Status: {status}
ID: {transaction_id}
Amount: RM{amount:.2f}
Date: {date_time}

Thank you for using our service!'''

print(transaction_message)