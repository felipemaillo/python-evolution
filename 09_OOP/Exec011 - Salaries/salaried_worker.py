from employee import Employee

class SalariedWorker(Employee):

  def __init__(self,name,gross_salary):
    super().__init__(name)
    self.gross_salary = gross_salary

  def calculate_salary(self):
    self.salary = self.gross_salary - (self.gross_salary * (Employee.social_security_tax / 100))