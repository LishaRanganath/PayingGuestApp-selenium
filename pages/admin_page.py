import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AdminPage():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_add_owner_button(self):
        self.driver.find_element(By.XPATH,"//div[@class='admin_action_buttons']/button[@id='add_owner_input']").click()
        time.sleep(2)

    def add_owner(self,name, phone, email, password):
        self.driver.find_element(By.XPATH,"//div/input[@id='name']").send_keys(name)
        self.driver.find_element(By.XPATH,"//div/input[@id='owner_phone']").send_keys(phone)
        self.driver.find_element(By.XPATH,"//div/input[@id='owner_user_attributes_email']").send_keys(email)
        self.driver.find_element(By.XPATH,"//div/input[@id='owner_user_attributes_password']").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[@class='form-container']/form/input[@type='submit']").click()
        time.sleep(2)
    def activate_owner(self,name):
        self.driver.find_element(By.XPATH,"//button/a[text()='Activate']").click()

        time.sleep(2)
        element = self.driver.find_element(By.XPATH," //table/tbody/tr/td[text() = '"+name+"']//following-sibling::td/form/button[text()='Activate']")
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()
        element.click()
        time.sleep(2)