from rich import inspect
from diary import Diary

def main():
  diary = Diary()
  diary.write('msg 1')
  diary.write('msg 2')
  diary.read('1234')
  diary.change_password('1234', '5678')
  diary.write('msg 3')
  diary.write('msg 4')
  diary.read('5678')

  inspect(diary, methods=True, private=True)

if __name__ == "__main__":
  main()
