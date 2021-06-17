from Backend.Services.account import Account
from Backend.Models.auth_payload import Payload
from Backend.Models.user import User
import pytest

class TestClass:

    account_service = Account()

    @pytest.mark.skip("Under Investigation")    
    def test_post_authorized_existing_user(self):
        user_data = User().default_user()
        data = Payload(username=user_data.username, password=user_data.password).to_dict()
        req = self.account_service.post_authorized(data)
        assert req.status_code == 200
        assert req.json() is not None
        assert isinstance(req.json(), bool)
        assert req.json() is True

    def test_post_authorized_new_user_generate_token_should_be_authorized(self, random_user):
        user_data = random_user[0]
        data = Payload(username=user_data.username, password=user_data.password).to_dict()
        req_generate_token = self.account_service.post_generate_token(data)
        assert req_generate_token.status_code == 200
        req = self.account_service.post_authorized(data)
        assert req.status_code == 200
        assert req.json() is not None
        assert isinstance(req.json(), bool)
        assert req.json() is True


    def test_post_authorized_wrong_password(self):
        data = Payload(username="ibrian93", password="MyTesting83?").to_dict()
        req = self.account_service.post_authorized(data)
        assert req.status_code == 404
        assert req.json() is not None
        assert req.json()["code"] == "1207", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "User not found!", "The message returned was: " + req.json()["message"]


    def test_post_non_authorized_user_missing_username(self):
        data = Payload(username=None, password="MyTesting83!").to_dict()
        req = self.account_service.post_authorized(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]


    def test_post_non_authorized_user_missing_password(self):
        data = Payload(username="ibrian93", password=None).to_dict()
        req = self.account_service.post_authorized(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]

    def test_post_authorized_user_not_found(self):
        data = Payload(username="string", password="string").to_dict()
        req = self.account_service.post_authorized(data)
        assert req.status_code == 404
        assert req.json() is not None
        assert req.json()["code"] == "1207", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "User not found!", "The message returned was: " + req.json()["message"]

    def test_post_authorized_user_null_body(self):
        req = self.account_service.post_authorized(data=None)
        assert req.status_code == 400
        assert req.json() is not None

    def test_post_authorized_user_with_invalid_body_empty_list(self):
        req = self.account_service.post_authorized(data=[])
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]

    def test_post_authorized_user_with_invalid_body_invalid_json(self):
        req = self.account_service.post_authorized(data="[]")
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]

    def test_post_created_user_but_no_generated_token(self, random_user):
        user_data = random_user[0]
        data = Payload(username=user_data.username, password=user_data.password).to_dict()
        req = self.account_service.post_authorized(data)
        assert req.status_code == 200
        assert req.json() is not None
        assert isinstance(req.json(), bool)
        assert req.json() is False