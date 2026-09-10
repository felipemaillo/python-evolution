from rich import print, inspect
from student import Student

def main():
  student = Student("Felipe", 1988, "ADM")
  student.add_course('STYLE')
  student.course = 'STYLE'
  student.birth_year = 2010
  inspect(student, methods=True, private=True)

if __name__ == "__main__":
  main()
