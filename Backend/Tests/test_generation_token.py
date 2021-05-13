from Backend.Services.account import Account

class TestClass:

    account_service = Account()

    def test_post_generation_token_successful(self):
        data = {"userName": "ibrian93", "password": "MyTesting83!"}
        req = self.account_service.post_generate_token(data)
        assert req.status_code == 200
        assert req.json() is not None
        assert isinstance(req.json()["token"], str)
        assert isinstance(req.json()["expires"], str)
        assert isinstance(req.json()["status"], str)
        assert isinstance(req.json()["result"], str)
        assert req.json()["status"] == "Success" and req.json()["result"] == "User authorized successfully."
