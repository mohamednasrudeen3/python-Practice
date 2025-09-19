class User:
    users = 0
    def __init__(self,username, pwd):
        self.username = username
        self.pwd = pwd
        User.users += 1


    def register(self):
        print("Registering..." + self.username)

    def login(self):
        print("Logging..."+ self.pwd)