import yaml


class Users:
    def __init__(self, filename='users.yaml') -> None:
        self.filename = filename
        self.users = {}
        self.initUsers()

    def initUsers(self):
        with open(self.filename, encoding='utf-8', mode='r') as f:
            self.users = yaml.safe_load(f)

    def getUsers(self):
        return self.users.get('users')

