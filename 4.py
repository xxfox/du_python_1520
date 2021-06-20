prices = [14.50, 26, 78.99, 10.5, 45, 89.09, 9, 10, 2.50, 1.4]
#A
price = ''
result = []
for item in prices:
    cents = int((item - int(item)) * 101)
    price = f'{int(item)} руб {cents:02d} копеек'
    result.append(price)
print(', '.join(result))
#B
print(prices)
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
#C
new_prices = sorted(prices, reverse=True)
print(new_prices)
#D
print(sorted(prices, reverse=True)[:5])






