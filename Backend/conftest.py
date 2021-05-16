import pytest

from Backend.Services.account import Account
from Backend.Models.user import User
from Backend.Models.auth_payload import Payload

@pytest.fixture
def random_user():
    random_user = User().random_user()
    data = Payload(username=random_user.username, password=random_user.password).to_dict()
    Account().post_user(data)
    import time
    time.sleep(0.5)
    return random_user
