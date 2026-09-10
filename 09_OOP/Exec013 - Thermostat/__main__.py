from thermostat import Thermostat

def main():
  thermostat = Thermostat(True)
  try:
    thermostat.temperature = 10
    thermostat.temperature = 40
  except Exception as error:
    print(f'Error changing temperature: {error}')

  print(f'Current temperature: {thermostat.f_temperature}')

if __name__ == "__main__":
  main()
