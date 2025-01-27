import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver

class Selenium:
    def __init__(self) -> None:
        """
        Initializes the Selenium class with the configured driver.
        """

        self.driver = self._init_driver(visual=True)

    def _init_driver(self, visual: bool) -> webdriver.Chrome:
        """
        Initializes the Chrome driver with the specified options.

        :param visual: Defines whether the browser should be started in visual or headless mode.
        :return: Instance of webdriver.Chrome.
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--force-device-scale-factor=1')

        if not visual:
            options.add_argument("--headless")
            options.add_argument('--window-size=1920,1080')

        service = ChromeService(ChromeDriverManager(driver_version="131.0.6778.265").install())
        driver = webdriver.Chrome(options=options, service=service)

        if visual:
            driver.maximize_window()
            
        return driver

    def close_driver(self) -> None:
        """
        Closes the browser and quits the WebDriver.
        """
        try:
            self.driver.quit()
            print("Driver successfully closed.")
        except Exception as e:
            print(f"An error occurred while closing the driver: {e}")
