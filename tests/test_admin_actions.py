import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_admin_actions(chrome_browser):
    driver = chrome_browser

    # To Land on the home page
    home_page = HomePage(driver)
    home_page.show()

    #To navigate to Login page and to login as admin
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login_as_admin("admin1@gmail.com","admin123")

    # To add 2 owners from the admin dashboard
    admin_page = AdminPage(driver)
    admin_page.navigate_to_add_owner_button()
    admin_page.add_owner("Lisha", "9435627845", "lisha@gmail.com", "lisha123")
    admin_page.navigate_to_add_owner_button()
    admin_page.add_owner("Shree", "9435627341", "shree@gmail.com", "shree123")

    # To activate a specific user and signout / logout
    admin_page.activate_owner("Lisha")
    login_page.logout()

    # Login as the activated owner to see if he/she lands on owner dashboard and logout
    login_page.login_as_admin("lisha@gmail.com", "lisha123")
    login_page.logout()

    #Login as the deactivated owner to check the error message displayed
    login_page.login_as_admin("shree@gmail.com", "shree123")
    login_page.logout()


