from .psw import Password
from .auth import Auth

class User(Password):
    def __init__(self):
        super().__init__()