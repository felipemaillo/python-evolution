# Exec 114
import requests

try:
  web_response = requests.get('https://www.pudim.com.br')
  print(f'The site https://www.pudim.com.br is on',f'Status code: {web_response.status_code}')
except:
  print(f'The site https://www.pudim.com.br is off')

# Exec 115
file = open('test.txt','w')
file.write(input('Say something: '))
file.close()

file = open('test.txt','r')
print(file.read())
file.close()