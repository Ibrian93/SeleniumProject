from Backend.Services.account import Account
from Backend.Models.auth_payload import Payload


class TestClass:

    account_service = Account()
    
    def test_deletion_account_successful(self, random_user):
        user_data = Payload(username=random_user.username, password=random_user.password).to_dict()
        req = self.account_service.post_user(data=user_data)
        req_user_id = req.json()["userId"]
        req_deletion = self.account_service.delete_user(req_user_id)
        assert req_deletion.status_code == 200