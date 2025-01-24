import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pandas import DataFrame

class AccessingURLs():
    def __init__(self, driver):
        self.driver = driver
        self.URL = 'https://www.sofascore.com/tournament/football/brazil/paulista-serie-a1/372#id:69522'

    def join_championship(self) -> None:
        timeout = 10  # Tempo total máximo de espera (segundos)
        interval = 1  # Intervalo entre tentativas (segundos)
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.driver.current_url == self.URL:
                return
            self.driver.get(self.URL)
            time.sleep(interval)

    def join_game(self, urls: DataFrame) -> None:
        print('a')