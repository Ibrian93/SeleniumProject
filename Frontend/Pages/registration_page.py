import Pages.login_page


class RegistrationPage:

    register_button = "register"
    back_to_login_button = "gotologin"

    def __init__(self, driver):
        self.driver = driver

    def register_user(self):
        self.driver.find_element_by_id(self.register_button).click()
        #check where it leads

    def back_to_login_page(self):
        self.driver.find_element_by_id(self.back_to_login_button).click()
        return Pages.LoginPage(self.driver)
