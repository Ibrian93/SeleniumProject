import Pages.login_page


class RegistrationPage:

    register_button = "register"
    back_to_login_button = "gotologin"
    first_name_input = "firstname"
    last_name_input = "lastname"
    username_input = "userName"
    password_input = "password"


    def __init__(self, driver):
        self.driver = driver

    def register_user(self):
        self.driver.find_element_by_id(self.register_button).click()
        #check where it leads

    def set_first_name(self, first_name):
        self.driver.find_element_by_id(self.first_name_input).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_id(self.last_name_input).send_keys(last_name)

    def set_username(self, username):
        self.driver.find_element_by_id(self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_input).send_keys(password)

    def input_registration_form(self, first_name, last_name, username, password):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_username(username)
        self.set_password(password)

    def back_to_login_page(self):
        self.driver.find_element_by_id(self.back_to_login_button).click()
        return Pages.LoginPage(self.driver)
