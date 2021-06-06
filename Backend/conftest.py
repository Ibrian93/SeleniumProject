import pytest

from Backend.Services.account import Account
from Backend.Models.user import User
from Backend.Models.auth_payload import Payload

@pytest.fixture
def random_user():
    random_user = User().random_user()
    random_user.password = random_user.password + "MyTesting83!"
    data = Payload(username=random_user.username, password=random_user.password).to_dict()
    req = Account().post_user(data)
    return random_user, req.json()
