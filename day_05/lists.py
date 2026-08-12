# list of shares
portfolio = ['Yari-Yari Inc., Jade Inc., Tenaga, TopGlov']

# indexing
first_share = portfolio[0]
last_share = portfolio[-1]

# slicing list
main_share = portfolio[0:2]

# list of stock value (in RM)
stock_value = [13000, 10000, 6000, 90000]

# total amount
total_value_of_stock = sum(stock_value)

# profit percentage of first share
percentage_of_Yari_Yari_Inc = (stock_value[0] / total_value_of_stock) * 100

print(f'total value of stock: RM{total_value_of_stock: .2f}')
print(f'Profit of first share: {percentage_of_Yari_Yari_Inc: .2f}%')