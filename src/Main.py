from Days import Day3, Day4
from common.DayFetcher import get_input_for_day


CURRENT_DAY = Day4


def Main():
  current_input = get_input_for_day(CURRENT_DAY)
  print(CURRENT_DAY.part1(current_input))

if __name__ == "__main__":
  Main()