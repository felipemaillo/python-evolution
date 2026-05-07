def format(price):
  return (f'$ {price:.2f}')

def increase(price, percentage, formatted=True):
  if formatted:
    return format(price + (price * percentage / 100))
  else:
    return price + (price * percentage / 100)

def decrease(price, percentage, formatted=True):
  if formatted:
    return format(price - (price * percentage / 100))
  else:
    return price - (price * percentage / 100)

def double(price, formatted=True):
  if formatted:
    return format(price * 2)
  else:
    return price * 2

def half(price, formatted=True):
  if formatted:
    return format(price / 2)
  else:
    return price / 2
  
def resume(price, percIncrease, percDecrease):
  print('-'*40)
  print(f'{'RESUME'.center(40)}')
  print('-'*40)
  print(f'Double: \t\t\t{double(price)}')
  print(f'Half: \t\t\t\t{half(price)}')
  print(f'Increasing by {percIncrease}%: \t\t{increase(price,percIncrease)}')
  print(f'Decreasing by {percDecrease}%: \t\t{decrease(price,percDecrease)}')
  print('-'*40)