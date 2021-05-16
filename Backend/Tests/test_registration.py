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