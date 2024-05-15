import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.sign_up_page import SignUpPage
from pages.building_page import BuildingPage


def test_owner_actions(chrome_browser):
    driver = chrome_browser

    # To Land on the home page
    home_page = HomePage(driver)
    home_page.show()

    # navigate to sign up page
    sign_up_page = SignUpPage(driver)
    sign_up_page.navigate_to_sign_up_page()


    #Sign up as user
    sign_up_page.sign_up("Lisha","32453684765","lishar12002@gmail.com","lisha123","lisha123")

    # apply the filters
    # sign_up_page.filter_buildings("Z-A","Double-Sharing","With-AC")
    # select a specific pg Building

    building_page = BuildingPage(driver)
    building_page.get_building_imformation()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='book_room'])[1]")))
    building_page.book_a_room()