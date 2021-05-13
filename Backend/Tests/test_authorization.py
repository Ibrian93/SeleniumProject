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
