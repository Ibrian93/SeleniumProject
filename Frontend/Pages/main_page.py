from Utils.environment import EnvironmentLoader
from Pages.login_page import LoginPage


store_book_url = EnvironmentLoader('environment').loader()

class MainPage:

    login_button = "login"

    def __init__(self, driver):
        self.driver = driver

    def go_to_main_page(self):
        self.driver.get(store_book_url["home_page"])

    def go_to_login_page(self):
        self.driver.find_element_by_id(self.login_button).click()
        return LoginPage(self.driver)
