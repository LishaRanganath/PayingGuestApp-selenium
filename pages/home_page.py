import time

from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.driver = driver


    def show(self):
        self.driver.get("http://127.0.0.1:3000")
        self.driver.maximize_window()
        time.sleep(3)