from Utils.environment import EnvironmentLoader
from Pages.login_page import LoginPage

store_book_url = EnvironmentLoader('environment').loader()

class MainPage:

    login_button = "login"
    username_field = "userName-value"
    title_page = "main-header"

    def __init__(self, driver):
        self.driver = driver

    def go_to_main_page(self):
        self.driver.get(store_book_url["home_page"])

    def get_title_page(self):
        return self.driver.find_element_by_class_name(self.title_page).text

    def get_logged_username(self):
        return self.driver.find_element_by_id(self.username_field).text

    def go_to_login_page(self):
        self.driver.find_element_by_id(self.login_button).click()
        return LoginPage(self.driver)
