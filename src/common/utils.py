import os
from typing import Callable, Generator
# import requests

CACHE_LOCATION = "__inputs__"

class SessionTokenStore: 
  __token = None

  def __init__(self) -> None:
    if not self.__token:
      self.__token = os.getenv("ADVENT_OF_CODE_SESSION_TOKEN")
    
  def get_token(self) -> str:
    return self.__token

def __fetch_input_for_day_from_server(day: int) -> str:
  url = "https://adventofcode.com/2024/day/{}/input".format(day)

  headers = {
    "Cookie": "session=" + SessionTokenStore().get_token()
  }
  response = requests.get(url, headers=headers)

def get_input_for_day(day: int) -> str:
  try:
    with open(f"inputs/day{day}_input.txt", "r") as f:
      return f.read()
  except FileNotFoundError:
    print("Input file not found, fetching from server")
    return fetch_input_for_day_from_server(day)

def get_input_lines_for_day(day: int) -> Generator[str]:
  with open(f"inputs/day{day}_input.txt", "r") as f:
    for line in f:
      yield line

def get_input_for_day(day: int) -> str:
  with open(f"inputs/day{day}_input.txt", "r") as f:
    return f.read()
  
def get_input_lines_parsed_for_day[T](day: int, parse: Callable[[str], T]) -> Generator[str]:
  with open(f"inputs/day{day}_input.txt", "r") as f:
    for line in f:
      yield parse(line)