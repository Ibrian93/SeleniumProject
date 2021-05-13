import requests


class Account:

    host = "https://demoqa.com"

    def post_generate_token(self, data, headers):
        endpoint = "/Account/v1/GenerateToken"
        r = requests.post(url=self.host + endpoint, data=data, headers=headers)
        return r
