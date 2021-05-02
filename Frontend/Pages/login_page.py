from Pages.registration_page import RegistrationPage


class LoginPage:

    login_button = "login"
    registration_button = "newUser"

    def __init__(self, driver):
        self.driver = driver

    def go_to_registration_page(self):
        self.driver.find_element_by_id(self.registration_button).click()
        return RegistrationPage(self.driver)

    def login_user(self):
        self.driver.find_element_by_id(self.login_button).click()
