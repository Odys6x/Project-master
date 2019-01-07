import shelve

class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.answer = ''

class Blacklist:
    def __init__(self):
        self.username = ''
        self.reason = ''

blacklist = shelve.open('blacklist')
users = shelve.open('users')


def get_user(username, password):
    if username in blacklist:
        return False
    elif username in users:
        user = users[username]
        if  user.password == password:
            return user
    return None

def create_user(username, password, answer):
    u = User()
    u.username = username
    u.password = password
    u.answer = answer
    users[username] = u

def cpassword(username, answer):
    if username in users:
        user = users[username]
        if user.answer == answer:
            return user
    return None


def npassword(username, password):
    user = users[username]
    user.password = password


def blacklistuser(username, reason):
    b = Blacklist()
    b.username = username
    b.reason = reason
    blacklist[username] = b