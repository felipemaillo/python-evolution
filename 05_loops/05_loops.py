# Exec 46
from time import sleep
print('Countdown to fireworks:')
for i in range(10, 0, -1):
  print(f'[{i}]')
  sleep(1)
print('Happy New Year! \U0001F386')

# Exec 47
print('Even numbers between 1 and 50:')
for i in range(2, 51, 2):
  print(i, end=' ')
print('')

# Exec 48
total_sum = 0
print('Sum of odd numbers divisible by 3 between 1 and 500:')
for i in range(1, 500, 2): 
  if i % 3 == 0:
    total_sum += i
print(f'Result: {total_sum}.')

# Exec 49
num = int(input('Enter a number: '))
print(f'Multiplication table for {num}: ')
for i in range(1, 11):
  print(f'[{num} x {i} = {i * num}]')

# Exec 50
total_sum = 0
for i in range(1, 7):
  num = int(input(f'Enter the {i}° integer: '))
  if num % 2 == 0:
    total_sum += num
print(f'The sum of the even numbers entered is: {total_sum}.')

# Exec 51
first_term = int(input('Enter the first term of the AP: '))
ratio = int(input('Enter the ratio of the AP: '))
tenth_term = first_term + (10 - 1) * ratio
print('The first 10 terms of the AP are: ')
for i in range(first_term, tenth_term + ratio, ratio):
  print(i, end=' ')
print('')

# Exec 52
num = int(input('Enter a number: '))
divisors = 0
for i in range(1, num + 1):
  if num % i == 0:
    print(f'\033[1;33m{i}\033[m', end= ' ')
    divisors += 1 
  else:
    print(f'\033[31m{i}\033[m', end= ' ')
print('')
print(f'The number {num} was divisible {divisors} times.')
if divisors == 2:
  print(f'So {num} is a prime number.')
else:
  print(f'So {num} is NOT a prime number.')

# Exec 53
text = input('Enter a sentence: ').strip().upper()
words = text.split()
joined = ''.join(words)
reversed_text = joined[::-1]
print(f'The reversed text is: {reversed_text}.')
if joined == reversed_text:
  print('The text is a palindrome.')
else:
  print('The text is NOT a palindrome.')

# Exec 54
from datetime import datetime
current_year = datetime.now().year
adults = 0
minors = 0
for i in range(1, 8):
  year = int(input(f'Enter birth year of person {i}: '))
  if current_year - year >= 18:
    adults += 1
  else:
    minors += 1
print(f'{adults} have reached adulthood.')
print(f'{minors} have not reached adulthood yet.') 

# Exec 55
weights = []
for i in range(1, 6):
  weights.append(float(input(f'Enter weight of person {i}: ')))
print(f'The highest weight entered was {max(weights):.2f} kg.')
print(f'The lowest weight entered was {min(weights):.2f} kg.')

# Exec 56
names = []
ages = []
genders = []

for i in range(1, 5):
  print(f'----- Person {i} -----')
  names.append(input('Enter name: '))
  ages.append(int(input('Enter age: ')))
  genders.append(input('Enter gender (M/F): ').strip().upper())

average_age = sum(ages) / len(ages)
print(f'The group average age is {average_age:.2f} years.')

females_under_20 = 0
for i in range(len(genders)):
  if genders[i] == 'F' and ages[i] < 20:
    females_under_20 += 1
print(f'Total of women under 20: {females_under_20}')

# Finding the oldest man
max_male_age = 0
oldest_man_name = ''
for i in range(len(genders)):
  if genders[i] == 'M' and ages[i] > max_male_age:
    max_male_age = ages[i]
    oldest_man_name = names[i]
if oldest_man_name:
    print(f'The oldest man is {max_male_age} years old and is called {oldest_man_name}.')

# Exec 57
gender = ''
while gender not in ['M','F']:
  gender = str(input('Enter gender (M/F): ')).strip().upper()
print(f'Gender recorded: {gender}.')

# Exec 58
import random
print('Computer picking a number between 0 and 10...')
pc_num = random.randint(0, 10)
guesses = 0
correct = False
while not correct:
  user_num = int(input('Which number did it choose? '))
  guesses += 1
  if user_num == pc_num:
    correct = True
  else:
    if user_num < pc_num:
        print('Higher...')
    else:
        print('Lower...')
print(f'Congrats! It took you {guesses} attempts.')

# Exec 59
option = 0
numbers = []
for i in range(1, 3):
  numbers.append(int(input(f'Enter number {i}: ')))
while option != 5:
  print('=-=' * 10)
  print('''Choose an option:
        [1] Sum
        [2] Multiply
        [3] Greater
        [4] New numbers
        [5] Exit program''')
  option = int(input('Enter option: '))
  if option == 1:
    print(f'Sum: {numbers[0] + numbers[1]}')
  elif option == 2:
    print(f'Product: {numbers[0] * numbers[1]}')
  elif option == 3:
    print(f'Greater: {max(numbers)}')
  elif option == 4:
    numbers = [int(input('New number 1: ')), int(input('New number 2: '))]
  elif option == 5:
    print('Exiting...')
  else:
    print('Invalid option.')

# Exec 60
num = int(input('Enter a number to calculate its factorial: '))
factorial = 1
print(f'Calculating {num}! = ', end='')
for i in range(num, 0, -1):
  factorial *= i
  print(f'{i}', end=' x ' if i > 1 else ' = ')
print(factorial)

# Exec 61
first_term = int(input('Enter first term: '))
ratio = int(input('Enter ratio: '))
count = 1
while count <= 10:
  print(f'{first_term} ', end='')
  first_term += ratio
  count += 1

# Exec 62
firstTerm = int(input('Enter the first term of the AP: '))
commonDifference = int(input('Enter the common difference: '))
tenthTerm = firstTerm + (10 - 1) * commonDifference

print('The first 10 terms of the AP are: ')
while firstTerm <= tenthTerm:
  print(firstTerm, end=' ')
  firstTerm += commonDifference
  print('')

numTerms = 1
while numTerms > 0:
  numTerms = int(input('Enter the number of additional terms you want to see: '))
  tenthTerm += commonDifference * numTerms
  while firstTerm <= tenthTerm:
    print(firstTerm, end=' ')
    firstTerm += commonDifference
    print('')

print('Program finished. Come back soon!')

# Exec 63
num = int(input('How many terms of the Fibonacci sequence? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
count = 3
while count <= num:
  t3 = t1 + t2
  print(f' -> {t3}', end='')
  t1 = t2
  t2 = t3
  count += 1
print(' -> END')

# Exec 64
num = 0
count = 0
total_sum = 0
num = int(input('Enter a number [999 to stop]: '))
while num != 999:
  total_sum += num
  count += 1
  num = int(input('Enter a number [999 to stop]: '))
print(f'You entered {count} numbers and the sum was {total_sum}.')

# Exec 65
num = 0
numbers = []
total_sum = 0
continue_asking = 'Y'
while continue_asking == 'Y':
  num = int(input('Enter a number: '))
  numbers.append(num)
  total_sum += num
  continue_asking = input('Do you want to continue? [Y/N] ').strip().upper()

print(f'You entered {len(numbers)} numbers.')
print(f'The numbers entered were: {numbers}.')
print(f'The average of the numbers entered is: {(total_sum / len(numbers)):.2f}.')
print(f'The largest number entered was: {max(numbers)}.')
print(f'The smallest number entered was: {min(numbers)}.')

# Exec 66
total_sum = count = 0
while True:
  n = int(input('Enter a value (999 to stop): '))
  if n == 999:
    break
  count += 1
  total_sum += n
print(f'The sum of the {count} values was {total_sum}!')

# Exec 67
while True:
  n = int(input('Want to see the table for which value? '))
  if n < 0:
    break
  for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')
print('Program closed.')

# Exec 68
from random import randint
wins = 0
while True:
  player = int(input('Enter a value: '))
  computer = randint(0, 10)
  total = player + computer
  choice = ' '
  while choice not in 'EO':
    choice = input('Even or Odd? [E/O] ').strip().upper()[0]
  print(f'You played {player} and computer {computer}. Total {total}')
  if choice == 'E':
    if total % 2 == 0:
      print('You won!')
      wins += 1
    else:
      print('You lost!')
      break
  elif choice == 'O':
    if total % 2 == 1:
      print('You won!')
      wins += 1
    else:
      print('You lost!')
      break
print(f'Game over! You won {wins} times.')

# Exec 69
over_18 = males = females_under_20 = 0
while True:
  age = int(input('Age: '))
  gender = ' '
  
  while gender not in 'MF':
    gender = input('Gender: [M/F] ').strip().upper()[0]
  if age >= 18:
    over_18 += 1
  if gender == 'M':
    males += 1
  if gender == 'F' and age < 20:
    females_under_20 += 1
  
  resp = ' '
  while resp not in 'YN':
    resp = input('Continue? [Y/N] ').strip().upper()[0]
  if resp == 'N':
    break
print(f'Adults: {over_18}, Men: {males}, Women < 20: {females_under_20}')

# Exec 70
total = over_1000 = cheapest_price = count = 0
cheapest_name = ''
while True:
  product = input('Product Name: ')
  price = float(input('Price: $'))
  count += 1
  total += price
  if price > 1000:
    over_1000 += 1
  if count == 1 or price < cheapest_price:
    cheapest_price = price
    cheapest_name = product
  resp = ' '
  while resp not in 'YN':
    resp = input('Continue? [Y/N] ').strip().upper()[0]
  if resp == 'N':
    break
print(f'Total: ${total:.2f}, Products > $1000: {over_1000}, Cheapest: {cheapest_name}')

# Exec 71
print('='*30)
print('ATM BANK')
print('='*30)
value = int(input('Withdraw amount: $'))
total = value
bill = 50
total_bills = 0
while True:
  if total >= bill:
    total -= bill
    total_bills += 1
  else:
    if total_bills > 0:
      print(f'Total of {total_bills} bills of ${bill}')
    if bill == 50:
      bill = 20
    elif bill == 20:
      bill = 10
    elif bill == 10:
      bill = 1
    total_bills = 0
    if total == 0:
      break