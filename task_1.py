from multiprocessing import Process
from time import sleep
import requests


class Time:

  def __init__(self, timeZone):
    self.timeZone = timeZone
    self.__current_time = {}

  def get_time(self):
    while True:
      request = requests.get(
          'https://www.timeapi.io/api/Time/current/zone?timeZone=' +
          self.timeZone)
      self.__current_time = request.json()
      print(f'Current time in Moscow: {self.__current_time["time"]}:{self.__current_time["seconds"]}')
      sleep(1)


if __name__ == '__main__':
  time = Time('Europe/Moscow')
  process_get = Process(target=time.get_time)
  process_get.start()
  process_get.join()
