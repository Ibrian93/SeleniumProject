from dataclasses import dataclass

payload = {'username': 'userName', 'password': 'password'}

@dataclass
class Payload:
    username: str = None
    password: str = None

    def to_dict(self):
        new_dict = {}
        for k, v in self.__dict__.items():
            new_dict[payload[k]] = v
        return new_dict
