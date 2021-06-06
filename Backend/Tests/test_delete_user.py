from Backend.Services.account import Account
from Backend.Models.auth_payload import Payload


class TestClass:

    account_service = Account()
    
    def test_deletion_account_successful(self, random_user):
        req_user_id = random_user[1]["userID"]
        user_data = random_user[0]
        data = Payload(username=user_data.username, password=user_data.password).to_dict()
        req = self.account_service.post_generate_token(data)
        auth_token = req.json()["token"]
        req_deletion = self.account_service.delete_user(user_id=req_user_id, auth_token=auth_token)
        assert req_deletion.status_code == 204

    def test_deletion_account_no_auth_token(self, random_user):
        req_user_id = random_user[1]["userID"]
        req_deletion = self.account_service.delete_user(user_id=req_user_id)
        assert req_deletion.status_code == 401
        assert req_deletion.json()["code"] == "1200"
        assert req_deletion.json()["message"] == "User not authorized!"
