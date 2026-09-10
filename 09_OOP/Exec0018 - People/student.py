from person import Person

class Student(Person):
  official_courses = ['ADM', 'ADS', 'ENG', 'CONT']

  def __init__(self, name:str, birth_year:int, course:str):
    super().__init__(name, birth_year)
    self._course = None
    self.course = course

  @property
  def course(self):
    return self._course

  @course.setter
  def course(self, course):
    if course in (Student.official_courses):
      self._course = course
    else:
      self._course = None
      raise ValueError(f'{course} is not available in the list of official courses.')

  def add_course(self, course):
    course = course.strip().upper()

    if 3 <= len(course) <= 5:
      if course not in Student.official_courses:
        Student.official_courses.append(course)
      else:
        raise ValueError('Course already exists.')
    else:
      raise ValueError(f'The name {course} is out of pattern. It must have 3 to 5 letters.')
