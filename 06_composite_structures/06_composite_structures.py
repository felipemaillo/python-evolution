# Exec 72
numbers = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
           'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
  num = int(input('Enter a number between 0 and 20: '))
  if 0 <= num <= 20:
    break
  print('Try again. ', end='')
print(f'You entered the number {numbers[num]}')

# Exec 73
teams = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Atlético PR', 'Bahia', 'Bragantino', 'Coritiba', 'Vitória', 'Botafogo',
         'Atlético Mineiro', 'Internacional', 'Vasco', 'Grêmio', 'Cruzeiro', 'Santos', 'Corinthians', 'Mirassol', 'Remo', 'Chapecoense')
print(f'Top 5: {teams[0:5]}')
print(f'Last 4: {teams[-4:]}')
print(f'Alphabetical: {sorted(teams)}')
print(f'Chapecoense is in position {teams.index("Chapecoense")+1}')

# Exec 74
from random import randint
nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Numbers: {nums}')
print(f'Max: {max(nums)}, Min: {min(nums)}')

# Exec 75
n = (int(input('Num: ')), int(input('Num: ')), int(input('Num: ')), int(input('Num: ')))
print(f'9 appeared {n.count(9)} times')
if 3 in n:
  print(f'3 was at position {n.index(3)+1}')
print('Evens: ', end='')
for i in n:
  if i % 2 == 0:
    print(i, end=' ')

# Exec 76
list = ('Coffee', 0.95, 'Croissant', 1.10, 'Juice', 1.65, 'Water', 1.10)
print('-'*40)
print(f'{"PRICE LIST":^40}')
print('-'*40)
for pos in range(len(list)):
  if pos % 2 == 0:
    print(f'{list[pos]:.<30}', end='')
  else:
    print(f'${list[pos]:>7.2f}')

# Exec 77
words = ('learn', 'program', 'python', 'course', 'study')
for w in words:
  print(f'\nIn word {w.upper()} we have vowels: ', end='')
  for letter in w:
    if letter.lower() in 'aeiou':
      print(letter, end=' ')

# Exec 78
list_num = []
for i in range(0, 5):
  list_num.append(int(input(f'Value for pos {i}: ')))
print(f'Max: {max(list_num)} at pos ', end='')
for i, v in enumerate(list_num):
  if v == max(list_num):
    print(f'{i}... ', end='')

# Exec 79
numbers = []
while True:
  n = int(input('Enter value: '))
  if n not in numbers:
    numbers.append(n)
    print('Added!')
  else:
    print('Duplicate!')
  r = input('Continue? [Y/N] ')
  if r in 'Nn':
    break
numbers.sort()
print(f'List: {numbers}')

# Exercise 80
numbers = []
for i in range(0, 5):
  num = int(input('Enter a value: '))
  if i == 0 or num > numbers[-1]:
    numbers.append(num)
    print('Value added to the end of the list.')
  else:
    for j in range(0, len(numbers)):
      if num <= numbers[j]:
        numbers.insert(j, num)
        print(f'Value added at position {j}.')
        break
print(f'The values entered in ascending order are: {numbers}')

# Exercise 81 
numbers = []
while True:
  numbers.append(int(input('Enter a value: ')))

  if input('Do you want to continue? [Y/N] ').strip().upper() == 'N':
    break

print(f'You entered {len(numbers)} numbers.')
numbers.sort(reverse=True)
print(f'The list in descending order would be: {numbers}')
print(f'Is the value 5 part of the list? {"Yes" if 5 in numbers else "No"}')

# Exercise 82
numbers = []
evens = []
odds = []
while True:
  numbers.append(int(input('Enter a value: ')))

  if input('Do you want to continue? [Y/N] ').strip().upper() == 'N':
    break

evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if not number % 2 == 0]

print(f'The entered list was: {numbers}')
print(f'The even numbers entered are: {evens}')
print(f'The odd numbers entered are: {odds}')

# Exercise 83
expression = input('Enter the expression: ')
stack = []

for symbol in expression:
  if symbol == '(':
    stack.append('(')
  elif symbol == ')':
    if len(stack) > 0:
      stack.pop()
    else:
      stack.append(')')
      break
print(f'The expression is correct.' if len(stack) == 0 else 'The expression is incorrect.')

# Exercise 84
people = []

while True:
  name = input('Enter the name: ')
  weight = float(input('Enter the weight: '))
  people.append([name, weight])

  if input('Do you want to continue? [Y/N] ').strip().upper() == 'N':
    break

print(f'{len(people)} people were registered.')
max_weight = max([person[1] for person in people])
min_weight = min([person[1] for person in people])
print(f'The heaviest weight was {max_weight} kg. Weight of {[person[0] for person in people if person[1] == max_weight]}')
print(f'The lightest weight was {min_weight} kg. Weight of {[person[0] for person in people if person[1] == min_weight]}')

# Exercise 85
numbers = [[],[]]
for i in range(0, 7):
  num = int(input(f'Enter the {i + 1}° integer value: '))
  if num % 2 == 0:
    numbers[0].append(num)
  else:
    numbers[1].append(num)

numbers[0].sort()
numbers[1].sort()
print(f'The even values entered were: {numbers[0]}')
print(f'The odd values entered were: {numbers[1]}')

# Exercise 86
matrix = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0, 3):
  for j in range(0, 3):
    matrix[i][j] = int(input(f'Enter a value for [{i},{j}]: '))

for i in range(0, 3):
  for j in range(0, 3): 
    print(f'[{matrix[i][j]:^5}]', end='')
  print('')
print('')

# Exercise 87
matrix = [[0,0,0],[0,0,0],[0,0,0]]
sum_evens = 0
sum_third_column = 0
max_second_row = 0

for i in range(0, 3):
  for j in range(0, 3):
    matrix[i][j] = int(input(f'Enter a value for [{i},{j}]: '))

for i in range(0, 3):
  for j in range(0, 3):
    if matrix[i][j] % 2 == 0:
      sum_evens += matrix[i][j]

    if j == 2:
      sum_third_column += matrix[i][j]

    if i == 1:
      if j == 0:
        max_second_row = matrix[i][j]
      elif matrix[i][j] > max_second_row:
        max_second_row = matrix[i][j]

    print(f'[{matrix[i][j]:^5}]', end='')
  print('')
print('')

print(f'The sum of even values is: {sum_evens}')
print(f'The sum of values in the third column is: {sum_third_column}')
print(f'The largest value in the second row is: {max_second_row}')

# Exercise 88
from random import randint

games = []
num_games = int(input('Enter the number of games to be created: '))

for i in range(0, num_games):
  numbers = [0,0,0,0,0,0]
  for j in range(0, 6): 
    while True:
      num = randint(1, 60)
      if num not in numbers:
        numbers[j] = num
        break

  games.append(numbers[:])

print('Games Created')
for i in range(0, num_games):
  games[i].sort()
  print(f'Game {i + 1}: {games[i]}')

# Exercise 89
students = []

while True:
  name = input('Enter the name: ')
  grade1 = float(input('Enter the first grade: '))
  grade2 = float(input('Enter the second grade: '))
  students.append([name, grade1, grade2])

  if input('Do you want to continue? [Y/N] ').strip().upper() == 'N':
    break

print('')
print('=' * 22)
print(f'{"REPORT CARD": ^22}')
print('=' * 22)
print(f'{"No.": <4}', end='')
print(f'{"Name": <10}', end='')
print(f'{"Average": >8}')

print('-' * 22)
for i in range(0, len(students)):
  print(f'{i: <4}', end='')
  print(f'{students[i][0]: <10}', end='')
  print(f'{(students[i][1] + students[i][2]) / 2:>8.1f}')
print('-' * 22)

while True:
  student_id = int(input('Enter student code to display grades. [999 to stop]: '))

  if student_id == 999:
    break
  if student_id <= len(students) - 1:
    print('')
    print(f'Grades for {students[student_id][0]} \nGrade 1: {students[student_id][1]} \nGrade 2: {students[student_id][2]}')
    print('-' * 22)
  else:
    print('Student not found. Please try again.')

# Exec 90
student = {}

student['name'] = input('Enter name: ')
student['average'] = float(input(f'Enter the average for {student["name"]}: '))
student['status'] = 'Approved' if student['average'] >= 7 else 'Failed' if student['average'] < 5 else 'Recovery'

for key, value in student.items():
  print(f'{key} is equal to {value}')

# Exec 91
from random import randint
from time import sleep
from operator import itemgetter

games = {
  'Player1': randint(1,6),
  'Player2': randint(1,6),
  'Player3': randint(1,6),
  'Player4': randint(1,6)
}
ranking = {}

print('Drawn values:')
for key, value in games.items():
  print(f'{key} rolled a {value} on the die.')
  sleep(1)

print('Player Ranking:')

ranking = sorted(games.items(), key=itemgetter(1), reverse=True)
for i, value in enumerate(ranking):
  print(f'{i + 1}st place: {value[0]} with {value[1]}') 
  sleep(1)

# Exec 92
from datetime import datetime

currentYear = datetime.now().year
person = {}

person['name'] = input('Enter name: ')
person['birthYear'] = int(input('Enter year of birth: '))
person['age'] = (currentYear - person['birthYear'])
person['workCard'] = int(input('Enter Work Card number (0 if none): '))

if person['workCard'] != 0:
  person['hiringYear'] = int(input('Enter hiring year: ')) 
  person['salary'] = float(input('Enter salary: $ '))
  person['retirementAge'] = (person['hiringYear'] + 35) - person['birthYear']
  print()
  print(f'{person["name"]} will retire at age {person["retirementAge"]} in the year {person["hiringYear"] + 35}')

for key, value in person.items():
  print(f'{key}: {value}')

# Exec 93
player = {}
goals = []

player['name'] = input('Enter player name: ')
player['matches'] = int(input(f'How many matches did {player["name"]} play? '))

for i in range(0, player['matches']):
  goals.append(int(input(f'Enter goals scored in match {i + 1}: ')))

player['goals'] = goals
player['totalGoals'] = sum(goals)

print('=' * 30)
print(player)
print('=' * 30)
print(goals)
print('=' * 30)

for key, values in player.items():
  print(f'Field {key} has the value {values}')

print('=' * 30)
print(f'Player {player["name"]} played {player["matches"]} matches')
print('=' * 30)

for i in range(0, player['matches']):
  print(f'In match {i + 1}, scored {player["goals"][i]} goals')
print('=' * 30)
print(f'It was a total of {player["totalGoals"]} goals.')
print('=' * 30)

# Exec 94
people = []
person = {}

while True:
  person['name'] = input('Enter name: ')
  person['gender'] = str(input('Enter gender [M/F]: ')).strip().upper()
  person['age'] = int(input('Enter age: '))
  people.append(person.copy())

  if input('Do you want to continue? [Y/N] ').strip().upper() == 'N':
    break

print('=' * 30)
print(people)
print('=' * 30)
print(f'Total people registered: {len(people)}.')
print('=' * 30)

averageAge = 0
for person in people:
  averageAge += person['age']
averageAge = averageAge / len(people)

print(f'The average age is {averageAge:.2f} years.')
print(f'Women in the list: {[person["name"] for person in people if person["gender"] == "F"]}')
print(f'People above average age: {[person for person in people if person["age"] > averageAge]}')
print('=' * 30)

# Exec 95
players = []
player = {}
goals = []

while True:
  player['name'] = input('Enter player name: ')
  player['matches'] = int(input(f'How many matches did {player["name"]} play? '))

  for i in range(0, player['matches']):
    goals.append(int(input(f'Enter amount of goals in match {i + 1}: ')))

  player['goals'] = goals.copy()
  player['totalGoals'] = sum(player['goals'])

  players.append(player.copy())
  goals.clear()
  print('_' * 30)

  if input('Do you want to continue? [Y/N] ').strip().upper() == 'N':
    break

print(f'Players: {players}')

print('')
print('=' * 40)
print(f'{"PLAYER DATA": ^40}')
print('=' * 40)
print(f'{"ID": <5}', end='')
print(f'{"Name": <10}', end='')
print(f'{"Goals": <20}', end='')
print(f'{"Total": <5}')
print('=' * 40)

for i in range(0, len(players)):
  print(f'{i: <5}', end='')
  print(f'{players[i]["name"]: <10}', end='')
  print(f'{str(players[i]["goals"]): <20}', end='')
  print(f'{players[i]["totalGoals"]: >5}')

while True:
  print('=' * 40)
  choice = int(input('Enter player ID to display performance [999 to exit]: '))

  if choice == 999:
    break
  if choice <= len(players) - 1:
    print('=' * 40)
    print(f'Performance review for player {players[choice]["name"]}')
    for j, g in enumerate(players[choice]['goals']):
      print(f'In match {j + 1}, scored {g} goals.')
  else:
    print('Player not found. Try again.')