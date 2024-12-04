def sign(x):
  if x < 0:
    return -1
  elif x > 0:
    return 1
  else:
    return 0

def test_report_v2(line):
  direction = 0
  for i in range(len(line) - 1):
    diff = line[i + 1] - line[i]
    
    if direction == 0:
      direction = sign(diff)
    elif sign(diff) != direction:
      return False

    if diff == 0 or abs(diff) > 3:
      return False

  return True

def test_report_with_damper(report):
  for i in range(len(report)):
    test_report = report[:i] + report[i+1:]
    res = test_report_v2(test_report)
    if res:
      return True
    
  return False


if __name__ == "__main__":
  res = 0
  with open("day2_input.txt", "r") as f:
    line_count = 0
    for line in f:
      line = [int(x) for x in line.split(" ")]
      line_count += 1

      if test_report_with_damper(line):
        res += 1
      else:
        print("Failed: ", line)

    print("Expected: ", line_count)
      

  print(res)