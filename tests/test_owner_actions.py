from pages.home_page import HomePage
from pages.sign_up_page import SignUpPage
from pages.building_page import BuildingPage
from pages.payments_page import PaymentsPage
from pages.login_page import LoginPage
from db.user import User
from db.booking import Booking
from db.building import Building
from db.room import Room


def test_owner_actions(chrome_browser):
    driver = chrome_browser

    # To Land on the home page
    home_page = HomePage(driver)
    home_page.show()

    # navigate to sign up page
    sign_up_page = SignUpPage(driver)
    sign_up_page.navigate_to_sign_up_page()

    # Sign up as user
    sign_up_page.sign_up("Lisha", "32453684765", "lishar12002@gmail.com", "lisha123", "lisha123")

    # apply the filters
    # sign_up_page.filter_buildings("Z-A","Double-Sharing","With-AC")

    # select a specific pg Building
    user_db = User()
    booking_db = Booking()
    building_db = Building()
    room_db = Room()
    payments_page = PaymentsPage(driver)
    user_id = user_db.get_user_id("lishar12002@gmail.com")

    building_page = BuildingPage(driver)
    building_page.get_building_imformation("Airbnb1")
    building_id = building_db.get_building_id("Airbnb1")
    room_id = building_page.book_a_room("18-05", 2, 2)
    print(room_id)
    room_count = room_db.check_current_room_count(room_id)
    print(room_count)

    payments_page.fill_payments_form("Lisha", "R", "4111111111111111", "09", "2026", "123")
    booking_id = booking_db.get_booking_id(user_id)
    booking_status = booking_db.get_booking_status(user_id)
    new_room_count = room_db.check_room_count(building_id, booking_id)
    assert new_room_count == room_count - 2
    assert booking_status == "success"

    login_page = LoginPage(driver)
    login_page.logout()

    login_page.login_as_admin("alec@gmail.com", "alec123")
    user_id = user_db.get_user_id("alec@gmail.com")
    role = user_db.check_role(user_id)
    assert role == ""
