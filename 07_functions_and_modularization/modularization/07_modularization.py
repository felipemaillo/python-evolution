# Exercise 107 and Exec 108 and Exec 109
# import currency

# price = float(input('Enter the price $: '))
# print(f'Half of {currency.format(price)} is {currency.half(price,False)}')
# print(f'Double of {currency.format(price)} is {currency.double(price)}')
# print(f'Increasing {currency.format(price)} by 10% we have {currency.increase(price, 10, False)}')
# print(f'Decreasing {currency.format(price)} by 13% we have {currency.decrease(price, 13)}')

# Exec 110 and Exec 111
# from utils import currency

# price = float(input('Enter the price $: '))
# currency.resume(price, 10, 13)

# Exec 112
from utils import data, currency

price = data.read_currency('Enter the price $: ')
currency.resume(price, 35, 22)