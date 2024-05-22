from selenium import webdriver
import time

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 10 seconds wait time

    def wait_for_element_to_be_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_for_element_to_be_present(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def wait_for_element_to_be_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))
