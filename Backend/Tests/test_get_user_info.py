from Backend.Services.account import Account
from Backend.Models.auth_payload import Payload

class TestClass:

    account_service = Account()

    def test_get_user_information_with_valid_data(self, random_user):
        req_user_id = random_user[1]["userID"]
        user_data = random_user[0]
        data = Payload(username=user_data.username, password=user_data.password).to_dict()
        req = self.account_service.post_generate_token(data)
        auth_token = req.json()["token"]
        req_user_info = self.account_service.get_user(user_id=req_user_id, auth_token=auth_token)
        assert req_user_info.status_code == 200
        assert req_user_info.json()["userId"] == req_user_id
        assert req_user_info.json()["username"] == user_data.username
