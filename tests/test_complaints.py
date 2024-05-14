import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.bookings_page import BookingsPage


def test_complaints_actions(chrome_browser):
    driver = chrome_browser

    # To Land on the home page
    home_page = HomePage(driver)
    home_page.show()

    # To navigate to Login page and to login as user
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login_as_admin("luke@gmail.com", "luke123")

    bookings_page = BookingsPage(driver)
    bookings_page.navigate_to_bookings_page()



