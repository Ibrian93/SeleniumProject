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

    def post_user(self, data, headers=None):
        endpoint = "/Account/v1/User"
        r = requests.post(url=self.host + endpoint, data=data, headers=headers)
        return r

    def delete_user(self, user_id, auth_token):
        endpoint = "/Account/v1/User/" + user_id
        headers = {'Authorization': "Bearer " + auth_token}
        r = requests.delete(url=self.host + endpoint, headers=headers)
        return r
