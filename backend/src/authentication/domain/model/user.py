from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str

    def __init__(self, username, password=""):
        self.username = username
        self.password = password

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return self.username == other.username
