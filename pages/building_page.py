import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BuildingPage():
    def __init__(self, driver):
        self.driver = driver

    def get_building_imformation(self, name):
        self.driver.find_element(By.XPATH,
                                 f"//p[text()='{name}']/ancestor::div[@class='content']/preceding-sibling::a/div/img").click()
        time.sleep(2)

    def book_a_room(self, date, number_of_guests, number_of_rooms):
        self.driver.refresh()
        element = self.driver.find_element(By.XPATH, "(//button[@id='book_room'])[1]")
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()
        room_id = element.get_attribute('data-room-id')
        element.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='date-select']").send_keys(date)
        self.driver.find_element(By.XPATH, "//select[@id='duration-select']").click()
        self.driver.find_element(By.XPATH, "//select[@id='duration-select']/option[@value=1]").click()
        self.driver.find_element(By.XPATH, "//input[@id='number-of-guests']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='number-of-guests']").send_keys(number_of_guests)
        self.driver.find_element(By.XPATH, "//input[@id='number-of-rooms']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='number-of-rooms']").send_keys(number_of_rooms)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(3)
        return room_id
