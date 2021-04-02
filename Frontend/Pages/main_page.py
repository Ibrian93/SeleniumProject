from Frontend.Utils.environment import EnvironmentLoader


store_url = EnvironmentLoader('environment').loader()

class MainPage:

    login_button = "login"

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.find_element_by_id(self.login_button).click()
        return LoginPage(self.driver)
