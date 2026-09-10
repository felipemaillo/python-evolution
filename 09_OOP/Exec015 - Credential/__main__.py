from credential import Credential

def main():
  credential = Credential()
  credential.password = input('Enter the password: ')
  if credential.validate(input('Confirm the password: ')):
    print('Password confirmed')
  else:
    print('Password not confirmed')

if __name__ == "__main__":
  main()
