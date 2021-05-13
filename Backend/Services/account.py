import requests


class Account:

    host = "https://demoqa.com"

    def post_generate_token(self, data, headers=None):
        endpoint = "/Account/v1/GenerateToken"
        r = requests.post(url=self.host + endpoint, data=data, headers=headers)
        return r

    def post_authorized(self, data, headers=None):
        endpoint = "/Account/v1/Authorized"
        r = requests.post(url=self.host + endpoint, data=data, headers=headers)
        return r
