from dataclasses import dataclass
from Backend.settings import DEFAULT_USER, DEFAULT_PASSWORD


@dataclass
class User:
    username: str = None
    password: str = None

    def default_user(self):
        self.username = DEFAULT_USER
        self.password = DEFAULT_PASSWORD
        return self
