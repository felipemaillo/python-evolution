from employee import Employee

class HourlyWorker(Employee):

  def __init__(self,name,hourly_rate = 7.37,hours_worked = 220):
    super().__init__(name)
    self.hourly_rate = hourly_rate
    self.hours_worked = hours_worked
    self.gross_salary = (self.hourly_rate * self.hours_worked)

  def calculate_salary(self):
    self.salary = self.gross_salary - (self.gross_salary * (Employee.social_security_tax / 100))