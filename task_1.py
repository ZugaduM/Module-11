from multiprocessing import Process
from time import sleep
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
import os


class Time:

  def __init__(self, timeZone):
    self.timeZone = timeZone
    self.__current_time = {}
    self.__clear = lambda: os.system('clear')
    self.__adapter = HTTPAdapter(max_retries=3)
    self.__session = requests.Session()
    self.__session.mount('https://www.timeapi.io', self.__adapter)

  def get_time(self):
    while True:
      try:
        request = self.__session.get(
            'https://www.timeapi.io/api/Time/current/zone?timeZone=' +
            self.timeZone)
        if request.status_code == 200:
          self.__current_time = request.json()
          print(f'Current time in Moscow: {self.__current_time["time"]}:{self.__current_time["seconds"]}')
        sleep(1)
        self.__clear()
      except ConnectionError as ce:
        print(ce)
        exit()


if __name__ == '__main__':
  time = Time('Europe/Moscow')
  process_get = Process(target=time.get_time)
  process_get.start()
  process_get.join()

