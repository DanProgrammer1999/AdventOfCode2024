import time
from common.DayFetcher import DayFetcher
from Config import AllDays, InputTypes

CURRENT_DAY = 3
PART = 1
INPUT_TYPE = InputTypes.real

def debug_input(input):
  pass

def debug_result(result):
  pass

def Main():
  fetcher = DayFetcher(CURRENT_DAY)

  if INPUT_TYPE == InputTypes.real:
    input = fetcher.get_input()
  else:
    input = fetcher.get_sample_input(INPUT_TYPE)
  
  debug_input(input)

  start = time.time()
  if PART == 1:
    result = AllDays[CURRENT_DAY].part1(input)
  else:
    result = AllDays[CURRENT_DAY].part2(input)

  end = time.time()

  print(f"--- TIME: {end - start: .6f} ---")

  debug_result(result)

  return result

if __name__ == "__main__":
  result = Main()

  print()
  print('------ RESULT ------')
  print(result)