import re


def part1(input: str) -> int:
  pass

def part2(input: str) -> int:
  res = 0
  expr = re.compile(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(don't)|(do)")
  
  matches = re.findall(expr, input)
  is_disabled = False
  for (a, b, disable, enable) in matches:
    if a and b and not is_disabled:
      res += int(a) * int(b)
    elif disable:
      is_disabled = True
    elif enable:
      is_disabled = False

  return res