from Days import Day3, Day4
from common.DayFetcher import DayFetcher


currentDay = Day4

days = {
  3: Day3,
  4: Day4
}

class PART:
  part1 = "part1"
  part2 = "part2"

class INPUT_TYPE:
  real = "real"
  sample = "sample"

  @staticmethod
  def custom_sample(custom_name):
    return f"{custom_name}"

def Main(day, part, input_type):
  fetcher = DayFetcher(day)

  if input_type == INPUT_TYPE.real:
    input = fetcher.get_input()
  else:
    input = fetcher.get_sample_input(input_type)
  
  if part == PART.part1:
    return days[day].part1(input)
  else:
    return days[day].part2(input)


if __name__ == "__main__":
  result = Main(4, PART.part2, INPUT_TYPE.real)
  print(result)