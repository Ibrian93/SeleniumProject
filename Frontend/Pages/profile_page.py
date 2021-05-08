class ProfilePage:

    title_page = "main-header"
    username_field = "userName-value"

    def __init__(self, driver):
        self.driver = driver

    def get_title_page(self):
        return self.driver.find_element_by_class_name(self.title_page).text

    def get_logged_username(self):
        return self.driver.find_element_by_id(self.username_field).text

