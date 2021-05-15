from dataclasses import dataclass


@dataclass
class User:
    username: str = None
    password: str = None
