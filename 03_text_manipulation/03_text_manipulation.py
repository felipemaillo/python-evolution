# Exec 23
num = int(input('Enter a number from 0 to 9999: '))
print(f'Units: {num % 10}')
print(f'Tens: {num // 10 % 10}')
print(f'Hundreds: {num // 100 % 10}')
print(f'Thousands: {num // 1000}')

# Exec 24
city = input('Enter the name of a city: ')
if city.strip().upper().startswith('SANTO'):
  print('The city starts with Santo.')
else: 
  print('The city does not start with Santo.')

# Exec 25
name = input('Enter your full name: ')
print('The name contains Silva.' if 'SILVA' in name.strip().upper() else 'The name does not contain Silva.')

# Exec 26
sentence = input('Enter a sentence: ').strip().upper()
print(f'The letter A appears {sentence.count("A")} times in the sentence.')
print(f'The first letter A appears at position {sentence.find("A") + 1}.')
print(f'The last letter A appears at position {sentence.rfind("A") + 1}.')

# Exec 27
name = input('Enter your full name: ')
print(f'First name: {name.split()[0]}')
print(f'Last name: {name.split()[-1]}')