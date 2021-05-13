from Backend.Services.account import Account

class TestClass:

    account_service = Account()

    def post_generation_token_successful(self):
        data = {"userName": "ibrian93", "password": "MyTesting83!"}
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        req = account_service.post_generate_token(data, headers)
        assert req.status_code == 200
        assert req.json() is not None
