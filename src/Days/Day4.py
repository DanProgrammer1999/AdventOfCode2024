####
##   * * * X M A S
##   * * M M M * *
##   * A * A * A *
##   S * * S * * S
##
##     |
##     |
##     v
##    --->
##    /  \
##   /    \
##  V      V
####

from enum import Enum

class Direction(Enum):
  VERTICAL = 1
  HORIZONTAL = 2
  DIAGONAL_LEFT = 3
  DIAGONAL_RIGHT = 4

def step_to(i, j, direction):
  if direction == Direction.VERTICAL:
    return i + 1, j
  elif direction == Direction.HORIZONTAL:
    return i, j + 1
  elif direction == Direction.DIAGONAL_LEFT:
    return i + 1, j - 1
  elif direction == Direction.DIAGONAL_RIGHT:
    return i + 1, j + 1
  
def test_limits(i, j, n, direction, grid):
  if direction == Direction.VERTICAL:
    return i + n < len(grid)
  elif direction == Direction.HORIZONTAL:
    return j + n < len(grid[i])
  elif direction == Direction.DIAGONAL_LEFT:
    return i + n < len(grid) and j - n >= 0
  elif direction == Direction.DIAGONAL_RIGHT:
    return i + n < len(grid) and j + n < len(grid[i])

def take_n_letters(i, j, n, direction, grid):
  if not test_limits(i, j, n - 1, direction, grid):
    return None

  res = ""
  for _ in range(n):
    res += grid[i][j]
    i, j = step_to(i, j, direction)

  return res

def search(i, j, target, direction, grid):
  text = take_n_letters(i, j, len(target), direction, grid)
  if text is None:
    return 0

  if text == target or text[::-1] == target:
    return 1

  return 0

def search_part_1(i, j, grid):
  return search(i, j, "XMAS", Direction.VERTICAL, grid) + search(i, j, "XMAS", Direction.HORIZONTAL, grid) + search(i, j, "XMAS", Direction.DIAGONAL_LEFT, grid) + search(i, j, "XMAS", Direction.DIAGONAL_RIGHT, grid)

def part1(input):
  grid = input.split("\n")
  grid = list(filter(lambda x: x != "", grid))
  res = 0

  for i in range(len(grid)):
    for j in range(len(grid[i])):
      res += search_part_1(i, j, grid)

  return res

def part2(input):
  grid = input.split("\n")
  grid = list(filter(lambda x: x != "", grid))

  res = 0

  for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
      diagonal1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
      diagonal2 = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
      if (diagonal1 == 'MAS' or diagonal1[::-1] == 'MAS') and (diagonal2 == 'MAS' or diagonal2[::-1] == 'MAS'):
        res += 1

  return res

      