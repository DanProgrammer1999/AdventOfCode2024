from Days import Day3
from common.utils import get_input_for_day


CURRENT_DAY = 3

solved_days = {
  3: Day3
}

def Main():
  current_input = get_input_for_day(CURRENT_DAY)
  print(solved_days[3].part2(current_input))

if __name__ == "__main__":
  Main()