from hourly_worker import HourlyWorker
from salaried_worker import SalariedWorker

def main():
  hourly_worker = HourlyWorker("Paulo",12,200)
  hourly_worker.calculate_salary()
  hourly_worker.analyze_salary()

  salaried_worker = SalariedWorker("Amanda",9500)
  salaried_worker.calculate_salary()
  salaried_worker.analyze_salary()

if __name__ == "__main__":
  main()