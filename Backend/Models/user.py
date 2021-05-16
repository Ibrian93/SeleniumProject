from dataclasses import dataclass
from Backend.settings import DEFAULT_USER, DEFAULT_PASSWORD
from faker import Faker


fake = Faker()

@dataclass
class User:
    username: str = None
    password: str = None

    def default_user(self):
        self.username = DEFAULT_USER
        self.password = DEFAULT_PASSWORD
        return self

    def random_user(self):
        Faker.seed()
        self.username = fake.simple_profile()["username"]
        self.password = fake.password()
        return self
