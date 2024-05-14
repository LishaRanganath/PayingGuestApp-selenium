import time

from selenium.webdriver.common.by import By


class BookingsPage():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_bookings_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//a[text()='Your-Bookings']").click()
        time.sleep(3)