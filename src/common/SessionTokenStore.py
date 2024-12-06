import os


class SessionTokenStore: 
  __token = None

  def __init__(self) -> None:
    if not self.__token:
      self.__token = os.getenv("ADVENT_OF_CODE_SESSION_TOKEN")
    
  def get_token(self) -> str:
    return self.__token
