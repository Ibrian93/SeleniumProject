from Backend.Services.account import Account

class TestClass:

    account_service = Account()

    def test_post_authorized_existing_user(self):
        data = {"userName": "ibrian93", "password": "MyTesting83!"}
        req = self.account_service.post_authorized(data)
        assert req.status_code == 200
        assert req.json() is not None
        assert isinstance(req.json(), bool)
        assert req.json() is True

    def test_post_non_authorized_user_invalid_username(self):
        data = {"userName": None, "password": "MyTesting83!"}
        req = self.account_service.post_authorized(data)
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200", "The code returned was: " + req.json()["code"]
        assert req.json()["message"] == "UserName and Password required.", "The message returned was: " + req.json()["message"]
