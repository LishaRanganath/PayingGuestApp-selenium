import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BuildingPage():
    def __init__(self, driver):
        self.driver = driver

    def get_building_imformation(self):
        self.driver.find_element(By.XPATH,"(//div[@class='image_container']/img)[1]").click()
        time.sleep(2)

    def book_a_room(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@id='book_room'])[1]").click()
        time.sleep(3)