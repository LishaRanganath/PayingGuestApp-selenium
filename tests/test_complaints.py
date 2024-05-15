import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.bookings_page import BookingsPage
from db.user import User

def test_complaints_actions(chrome_browser):
    driver = chrome_browser

    # To Land on the home page
    home_page = HomePage(driver)
    home_page.show()

    # To navigate to Login page and to login as user
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login_as_admin("lishar2002@gmail.com", "lisha123")
    user_db = User()
    user_id = user_db.get_user_id("lishar2002@gmail.com")

    bookings_page = BookingsPage(driver)
    bookings_page.navigate_to_bookings_page()
    bookings_page.add_complaints()

    login_page.logout()
    login_page.navigate_to_login_page()
    login_page.login_as_admin("alec@gmail.com", "alec123")

    bookings_page.navigate_to_complaints()

    status = user_db.check_complaints(user_id)
    assert status is not None
