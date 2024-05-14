import time

from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver


    def navigate_to_login_page(self):
        self.driver.find_element(By.XPATH, "//li/form/button[text()='SignIn']").click()
        time.sleep(2)

    def login_as_admin(self,email,password):
        self.driver.find_element(By.XPATH, "//div[@class ='field']/input[@id='user_email']").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@class='field']/input[@id='user_password']").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@class='login-actions']/input[@type='submit']").click()
        time.sleep(1)

    def logout(self):
        self.driver.find_element(By.XPATH, "//button[text()='SignOut']").click()
        time.sleep(2)