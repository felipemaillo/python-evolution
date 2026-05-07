def read_float(prompt):
  value = 0
  while True:
    try:
      value = float(input(prompt))
      break
    except ValueError:
      print('\033[31mERROR! Please enter a valid float.\033[m')
  
  return value

def read_int(prompt):
  value = 0
  while True:
    try:
      value = int(input(prompt))
      break
    except ValueError:
      print('\033[31mERROR! Please enter a valid integer.\033[m')

  return value