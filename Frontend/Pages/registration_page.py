import Pages.login_page


class RegistrationPage:

    register_button = "register"
    back_to_login_button = "gotologin"
    first_name_input = "firstname"
    last_name_input = "lastname"
    username_input = "userName"
    password_input = "password"
    iframe_tag = "iframe"
    recaptcha_checkbox = "recaptcha-checkbox-border"

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

    def select_recaptcha_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name(self.iframe_tag))

    def check_recaptcha_checkbox(self):
        self.driver.find_element_by_class_name(self.recaptcha_checkbox).click()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def input_registration_form(self, first_name, last_name, username, password):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_username(username)
        self.set_password(password)
        import time
        time.sleep(3)
        self.select_recaptcha_iframe()
        self.check_recaptcha_checkbox()
        self.switch_to_default_content()

    def back_to_login_page(self):
        self.driver.find_element_by_id(self.back_to_login_button).click()
        return Pages.LoginPage(self.driver)
