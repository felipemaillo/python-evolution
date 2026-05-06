# Exec 01
print('Hello, World!')

# Exec 02
name = input('Enter your name: ')
print(f'It is a pleasure to meet you, {name}!')

# Exec 03
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
total_sum = num1 + num2
print(f'The sum between {num1} and {num2} is equal to {total_sum}.')
 
# Exec 04
value = input('Type something: ')
print(f'The primitive type of this value is {type(value)}')
print(f'Does it only have spaces? {value.isspace()}')
print(f'Is it a number? {value.isnumeric()}')
print(f'Is it alphabetical? {value.isalpha()}')
print(f'Is it alphanumeric? {value.isalnum()}')
print(f'Is it in uppercase? {value.isupper()}')
print(f'Is it in lowercase? {value.islower()}')
print(f'Is it capitalized? {value.istitle()}')

# Exec 05
num = int(input('Enter a number: '))
print(f'The successor of {num} is {num + 1}.')
print(f'The predecessor of {num} is {num - 1}.')

# Exec 06
num = int(input('Enter a number: '))
print(f'The double of {num} is {num * 2}.')
print(f'The triple of {num} is {num * 3}.')
print(f'The square root of {num} is {num ** (1/2):.2f}.')

# Exec 07
grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))
average = (grade1 + grade2) / 2
print(f'The average between {grade1} and {grade2} is equal to {average}.')

# Exec 08
meters = float(input('Enter a distance in meters: '))
print(f'The distance of {meters} meters corresponds to:')
print(f'{meters * 100} centimeters.')
print(f'{meters * 1000} millimeters.')

# Exec 09
num = int(input('Enter a number: '))
print(f'The multiplication table for {num} is: ')
for i in range(1, 11):
  print(f'[{num} x {i} = {i * num}]')

# Exec 10
amount = float(input('Enter the amount you have in your wallet: $ '))
dollar = amount / 5.17
print(f'With ${amount:.2f} you can buy US${dollar:.2f}.')

# Exec 11
width = float(input('Enter the wall width: '))
height = float(input('Enter the wall height: '))
area = width * height
paint = area / 2
print(f'The wall area is {area:.2f} m².')
print(f'The amount of paint needed to paint the wall is {paint:.2f} liters.')

# Exec 12
price = float(input('Enter the price: $ '))
discount_price = price * 0.95
print(f'The price with a 5% discount is ${discount_price:.2f}.')

# Exec 13
salary = float(input('Enter the salary: $ '))
new_salary = salary * 1.15
print(f'The salary with a 15% increase is ${new_salary:.2f}.')

# Exec 14
tempC = float(input('Enter the temperature in °C: '))
tempF = (tempC * 9/5) + 32
print(f'The temperature of {tempC:.2f}°C corresponds to {tempF:.2f}°F.')

# Exec 15
km = float(input('Enter the distance in km: '))
days = int(input('Enter the number of days: '))
total = (60 * days) + (0.15 * km)
print(f'The total to pay is $ {total:.2f}.')