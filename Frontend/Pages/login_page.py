from Pages.registration_page import RegistrationPage
import Pages.main_page

class LoginPage:

    login_button = "login"
    registration_button = "newUser"
    username_field = "userName"
    password_field = "password"
    error_message_field = ".mb-1"


    def __init__(self, driver):
        self.driver = driver

    def go_to_registration_page(self):
        self.driver.find_element_by_id(self.registration_button).click()
        return RegistrationPage(self.driver)

    def set_username(self, username):
        self.driver.find_element_by_id(self.username_field).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_field).send_keys(password)

    def login_user_form(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.login_user()
        return Pages.main_page.MainPage(self.driver)

    def login_user(self):
        self.driver.find_element_by_id(self.login_button).click()

    def get_error_message(self):
        error_message = self.driver.find_element_by_css_selector(self.error_message_field).text
        return error_message

