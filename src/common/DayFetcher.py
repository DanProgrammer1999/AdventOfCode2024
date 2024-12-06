import requests

from common.SessionTokenStore import SessionTokenStore

CACHE_LOCATION = "__inputs__"


def get_input_file_name(day: int) -> str:
  return f"{CACHE_LOCATION}/day{day}_input.txt"

class DayFetcher:
  def __init__(self, day: int) -> None:
    self.day = day

  def get_input(self) -> str:
    try:
      with open(get_input_file_name(self.day), "r") as f:
        return f.read()
    except FileNotFoundError:
      print("Input file not found, fetching from server")
      return self.__fetch_input_for_day_from_server()

  def __fetch_input_for_day_from_server(self) -> str:
    url = "https://adventofcode.com/2024/day/{}/input".format(self.day)

    headers = {
      "Cookie": "session=" + SessionTokenStore().get_token()
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
      raise Exception("Failed to fetch input from server")
    else:
      with open(get_input_file_name(self.day), "w") as f:
        f.write(response.text)
      return response.text
    
  def get_sample_input(self, sample_file_name="sample"):
    with open(f"{CACHE_LOCATION}/day{self.day}_{sample_file_name}.txt", "r") as f:
      return f.read()