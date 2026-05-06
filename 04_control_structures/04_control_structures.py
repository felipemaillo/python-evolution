# Exec 28
import random
print('Computer choosing a number between 0 and 5...')
pc_num = random.randint(0, 5)
user_num = int(input('Which number did the computer choose? '))
if pc_num == user_num:
  print('Congratulations, you got it right!')
else:
  print(f'You missed, the number chosen by the computer was {pc_num}.')

# Exec 29
speed = float(input('Enter the car speed in km/h: '))
if speed > 80:
  fine = (speed - 80) * 7
  print(f'You were fined $ {fine:.2f} for exceeding the speed limit.')
else:
  print('You are within the speed limit.')

# Exec 30
num = int(input('Enter an integer: '))
if num % 2 == 0:
  print(f'The number {num} is even.')
else:
  print(f'The number {num} is odd.')

# Exec 31
km = float(input('Enter the travel distance in km: '))
if km <= 200:
  ticket_price = km * 0.50
else:
  ticket_price = km * 0.45
print(f'The ticket price is $ {ticket_price:.2f}.')

# Exec 32
year = int(input('Enter a year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f'The year {year} is a leap year.')
else:
  print(f'The year {year} is not a leap year.')

# Exec 33
numbers = []
numbers.append(int(input('Enter the first number: ')))
numbers.append(int(input('Enter the second number: ')))
numbers.append(int(input('Enter the third number: ')))
print(f'The largest number is {max(numbers)}.')
print(f'The smallest number is {min(numbers)}.')

# Exec 34
salary = float(input('Enter the employee salary: $ '))
if salary > 1250:
  new_salary = salary * 1.10
else:
  new_salary = salary * 1.15
print(f'The new employee salary is $ {new_salary:.2f}.')

# Exec 35
l1 = float(input('Enter the length of the first line: '))
l2 = float(input('Enter the length of the second line: '))
l3 = float(input('Enter the length of the third line: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
  print('The lines form a triangle.')
else:
  print('The lines do not form a triangle.')

# Exec 36
house_value = float(input('Enter the house value: $ '))
salary = float(input('Enter the buyer salary: $ '))
payment_years = int(input('Enter how many years to pay: '))

installment = house_value / (payment_years * 12)
if installment > salary * 0.30:
  print(f'Loan denied. The installment of $ {installment:.2f} exceeds 30% of the buyer salary.')
else:
  print(f'Loan approved. The installment of $ {installment:.2f} is compatible with the buyer salary.')

# Exec 37
num = int(input('Enter a number: '))
base = int(input('Enter the conversion base (1 for binary, 2 for octal, 3 for hexadecimal): '))

if base == 1:
  print(f'The number {num} in binary is {bin(num)[2:]}.')
elif base == 2:
  print(f'The number {num} in octal is {oct(num)[2:]}.')
elif base == 3:
  print(f'The number {num} in hexadecimal is {hex(num)[2:].upper()}.')
else:
  print('Invalid conversion base. Please choose 1, 2, or 3.')

# Exec 38
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
if num1 > num2:
  print(f'{num1} is greater than {num2}.')
elif num2 > num1:
  print(f'{num2} is greater than {num1}.')
else:
  print(f'Both numbers are equal.')

# Exec 39
import datetime

birth_year = int(input('Enter birth year: '))
age = datetime.datetime.now().year - birth_year

if age < 18:
  print(f'There are still {18 - age} years left for enlistment.')
elif age == 18:
  print('It is time to enlist.')
else:
  print(f'It has been {age - 18} years since the enlistment time.')

# Exec 40
grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))
average = (grade1 + grade2) / 2
if average < 5.0:
  print(f'With an average of {average:.1f}, the student failed.')
elif 5.0 <= average < 7.0:
  print(f'With an average of {average:.1f}, the student is in recovery.')
else: 
  print(f'With an average of {average:.1f}, the student passed.')

# Exec 41
import datetime
birth_year = int(input('Enter birth year: '))
age = datetime.datetime.now().year - birth_year
if age <= 9:
  print(f'At {age} years old, the athlete is in the LITTLE category.')
elif age <= 14:
  print(f'At {age} years old, the athlete is in the INFANT category.')
elif age <= 19:
  print(f'At {age} years old, the athlete is in the JUNIOR category.')
elif age <= 25:
  print(f'At {age} years old, the athlete is in the SENIOR category.')
else:
  print(f'At {age} years old, the athlete is in the MASTER category.')

# Exec 42
l1 = float(input('Enter the length of the first line: '))
l2 = float(input('Enter the length of the second line: '))
l3 = float(input('Enter the length of the third line: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
  if l1 == l2 == l3:
    print('The lines form an equilateral triangle.')
  elif l1 == l2 or l1 == l3 or l2 == l3:
    print('The lines form an isosceles triangle.')
  else:
    print('The lines form a scalene triangle.')
else:
  print('The lines do not form a triangle.')

# Exec 43
weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in meters: '))
bmi = weight / (height ** 2)

if bmi < 18.5:
  print(f'With a BMI of {bmi:.1f}, the person is underweight.')
elif bmi < 25:
  print(f'With a BMI of {bmi:.1f}, the person has ideal weight.')
elif bmi < 30:
  print(f'With a BMI of {bmi:.1f}, the person is overweight.')
elif bmi < 40:
  print(f'With a BMI of {bmi:.1f}, the person is obese.')
else:
  print(f'With a BMI of {bmi:.1f}, the person has morbid obesity.')

# Exec 44
price = float(input('Enter the product price: $ '))
print('''Choose payment method:
[1] Cash/Check (10% off)
[2] Credit Card (5% off)
[3] 2x on Card (standard price)
[4] 3x or more on Card (20% interest)''')
option = int(input('Enter payment option: '))

if option == 1:
  final_price = price * 0.90
elif option == 2:
  final_price = price * 0.95
elif option == 3:
  final_price = price
elif option == 4:
  installments = int(input('Enter the number of installments: '))
  final_price = price * 1.20
  print(f'Your purchase, with interest, will be in {installments} installments of $ {final_price / installments:.2f}.')
else:
  print('Invalid option.')

print(f'The final product price is $ {final_price:.2f}.')

# Exec 45
from random import randint
options = ['rock', 'paper', 'scissors']
print('Let\'s play Rock-Paper-Scissors!')
print('Choose an option: \n [1] Rock \n [2] Paper \n [3] Scissors')
user_choice = int(input('Enter your choice: '))
if not user_choice in [1, 2, 3]:
  print('Invalid option.')
else:
  pc_choice = randint(0, 2)
  print(f'You chose {options[user_choice - 1]} and the computer chose {options[pc_choice]}.')
  if user_choice - 1 == pc_choice:
    print('It\'s a tie!')
  elif (user_choice - 1 == 0 and pc_choice == 2) or (user_choice - 1 == 1 and pc_choice == 0) or (user_choice - 1 == 2 and pc_choice == 1):
    print('Congratulations, you won!')
  else:
    print('You lost. Try again!')