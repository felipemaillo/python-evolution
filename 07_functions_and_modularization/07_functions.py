# Exec 96
def area(width, height):
  return (width * height)

width = float(input('Enter the Width (m): '))
height = float(input('Enter the Height (m): '))

print(f'The area of a {width}x{height} land is: {str(area(width, height))}m2')

# Exec 97
def write(text):
  size = (len(text) + 4)
  print('-' * size)
  print(f'{text: ^{size}}')
  print('-' * size)

write('Hello World!')
write('Hi!')
write('Longer text string test')

# Exec 98
def counter(start, end, step):
  print('-' * 30)
  print(f'Counting from {start} to {end} by {step}s.')
  
  if end < start:
    end -= 1
  else:
    end += 1

  for i in range(start, end, step):
    print(f'{i}', end=' ')
  print('DONE!')
  print('-' * 30)

counter(1, 10, 1)
counter(10, 0, -2)

print('Create your own custom count')
start_val = int(input('Enter the start value: '))
end_val = int(input('Enter the end value: '))
step_val = int(input('Enter the step value: '))

counter(start_val, end_val, step_val)

# Exec 99
def find_max(*numbers):
  print('Analyzing the values provided...')
  max_val = 0
  for number in numbers:
    if number > max_val:
      max_val = number

  print(f'{len(numbers)} numbers were provided, which are: {numbers}.')
  print(f'The largest value provided was: {max_val}')

find_max(1, 4, 6, 7, 3, 6, 643, 8, 9, 5, 3, 3, 55)

# Exec 100
from random import randint

def sum_even(num_list):
  even_sum = 0
  for i in range(0, len(num_list)):
    if num_list[i] % 2 == 0:
      even_sum += num_list[i]

  print(f'The sum of the even numbers in the list is: {even_sum}')

def draw():
  num_list = []
  for i in range(1, 6):
    num_list.append(randint(0, 10))

  print(f'Randomly drawn list: {num_list}')
  return num_list

sum_even(draw())

# Exec 101
from datetime import datetime
age = datetime.now().year

def voting_status(birth_year):
  global age

  age -= birth_year

  if age < 16:
    return 'DENIED'
  elif age < 18:
    return 'OPTIONAL'
  else:
    return 'MANDATORY'

status = voting_status(int(input('Enter your birth year: ')))
print(f'At {age} years old, your voting status is: {status}')

# Exec 102
def factorial(number, show=False):
  """
  -> factorial: Calculates the factorial of a number.
  :param number: The number to be calculated.
  :param show: True: to display the calculation process. Default is False.
  :return: Returns the total value of the calculation.
  """
  total = 1
  for i in range(number, 0, -1):
    total *= i
    if show:
      print(f'{i}{" x " if i != 1 else ""}', end='')
  
  return total

num = int(input('Enter a number to see its factorial: '))
display_calc = True if str(input('Do you want to see the calculation process? [Y/N]: ')).strip().upper() == 'Y' else False
print(f'\nThe factorial of {num} is: {factorial(num, display_calc)}')

# Exec 103
def score_sheet(name='<unknown>', goals=0):
  print(f'Player {name} scored {goals} goal(s) in the championship.')

player_name = str(input("Enter player's name: "))
goals_scored = input('Enter number of goals scored: ')

if goals_scored.isnumeric():
  goals_scored = int(goals_scored)
else:
  goals_scored = 0

if player_name.strip() == '':
  score_sheet(goals=goals_scored)
else:
  score_sheet(player_name, goals_scored)

# Exec 104
def read_int(prompt):
  value = 0
  while True:
    try:
      value = int(input(prompt))
      break
    except ValueError:
      print('\033[31mERROR! Please enter a valid integer.\033[m')
  
  return value

n = read_int('Enter an integer: ')
print(f'You entered the number: {n}')

# Exec 105
def grades(*grades_list, status=False):
  """
  -> grades: Function to analyze grades and status of multiple students.
  :param grades_list: One or more student grades (accepts multiple values).
  :param status: Optional value, indicating whether to add the class status.
  :return: Dictionary with information about the class performance.
  """
  grade_info = {}
  grade_info['total'] = len(grades_list)
  grade_info['highest'] = max(grades_list)
  grade_info['lowest'] = min(grades_list)
  grade_info['average'] = (sum(grades_list) / len(grades_list))
  
  if status:
    if grade_info['average'] >= 7:
      grade_info['status'] = 'GOOD'
    elif grade_info['average'] >= 5:
      grade_info['status'] = 'AVERAGE'
    else:
      grade_info['status'] = 'POOR'

  return grade_info   

print(grades(5.5, 9.5, 10, 6.5, status=True))

# Exec 106
while True:
  command = input('Enter the function name you need help with (or "QUIT" to exit): ').strip()

  if command.upper() == 'QUIT':
    break

  print(help(command))
  