import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class PaymentsPage():
    def __init__(self, driver):
        self.driver = driver

    def fill_payments_form(self,first_name,last_name,card_number,month,year,cvv):
        self.driver.refresh()
        self.driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys(first_name)
        self.driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//input[@id='number']").send_keys(card_number)
        self.driver.find_element(By.XPATH, "//input[@id='month']").send_keys(month)
        self.driver.find_element(By.XPATH, "//input[@id='year']").send_keys(year)
        self.driver.find_element(By.XPATH, "//input[@id='verification_value']").send_keys(cvv)
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(6)
        element= self.driver.find_element(By.XPATH,"//a[text()='Download Invoice']")
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()
        element.click()



