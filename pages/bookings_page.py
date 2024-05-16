import time

from selenium.webdriver.common.by import By


class BookingsPage():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_bookings_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text()='Your-Bookings']").click()
        time.sleep(3)
    def add_complaints(self):
        self.driver.find_element(By.XPATH,"//input[@id='booking_complaints']").send_keys("Good")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)

    def navigate_to_complaints(self):
        self.driver.find_element(By.XPATH,"//a[text()='Compalints']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Approve'])[1]").click()
        time.sleep(2)