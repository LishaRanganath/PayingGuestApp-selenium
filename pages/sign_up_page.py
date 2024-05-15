import time

from selenium.webdriver.common.by import By

class SignUpPage():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_sign_up_page(self):
        self.driver.find_element(By.XPATH,"//a[text()='SignUp']").click()
        time.sleep(2)

    def sign_up(self,name,phone,email,password,confirm_password):
        self.driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@id='user_phone']").send_keys(phone)
        self.driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='user_password_confirmation']").send_keys(confirm_password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(2)

    def filter_buildings(self,type,room_type,category):

        self.driver.find_element(By.XPATH,"//select[@id='filter-select']").click()
        self.driver.find_element(By.XPATH,f"//select[@id='filter-select']/option[text()='{type}']").click()
        self.driver.find_element(By.XPATH, f"//select[@id='room-select']").click()
        self.driver.find_element(By.XPATH, f"//select[@id='room-select']/option[text()='{room_type}']").click()
        self.driver.find_element(By.XPATH, f"//select[@id='category-select']").click()
        self.driver.find_element(By.XPATH,f"//select[@id='category-select']/option[text()='{category}']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@id='filter-btn']").click()
        time.sleep(120)

