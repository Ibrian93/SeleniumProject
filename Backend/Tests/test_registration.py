from Backend.Models.user import User
from Backend.Services.account import Account
from Backend.Models.auth_payload import Payload


class TestClass:

    account_service = Account()

    def test_post_user_valid_data(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password=user_data.password).to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 201
        assert isinstance(req.json()["userID"], str)
        assert isinstance(req.json()["username"], str)
        assert isinstance(req.json()["books"], list)
        assert req.json() is not None
        assert req.json()["username"] == user_data.username
        assert req.json()["userID"] != ""
        assert req.json()["books"] == []

    def test_post_user_invalid_data_missing_username(self):
        user_data = User().random_user()
        data = Payload(username=None, password=user_data.password).to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_data_missing_password(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password=None).to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]
    
    def test_post_user_invalid_data_missing_username(self):
        user_data = User().random_user()
        data = Payload(username=None, password=user_data.password).to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_data_invalid_password_criteria_only_digits(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="12345678").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_data_password_empty_space(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password=" ").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_data_password_only_upper_case(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="TESTINGS").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]
    
    def test_post_user_invalid_data_password_only_lower_case(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="testings").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_data_password_only_special_characters(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="!@#$%^&*").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_data_password_only_upper_case(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="TESTINGS").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_password_missing_criteria_lower_case(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="T3ST!NGS").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_password_missing_criteria_special_character(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="T3stings").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_password_missing_criteria_upper_case(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="t3st!ngs").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

    def test_post_user_invalid_password_missing_criteria_digits(self):
        user_data = User().random_user()
        data = Payload(username=user_data.username, password="Test!ngs").to_dict()
        req = self.account_service.post_user(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1300", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.", "The message returned was: " + req.json()["message"]

