from abc import ABCMeta, abstractmethod


class DailySolutio(ABCMeta):
  @abstractmethod
  def day1(self):
    pass

  @abstractmethod
  def day2(self):
    pass
