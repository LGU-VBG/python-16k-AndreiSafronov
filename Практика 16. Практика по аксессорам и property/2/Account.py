from hash import hash_function

class Account:
    def __init__(self, login, password):
        self._login = login
        self._password_hash = hash_function(password)
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, value):
        raise AttributeError('Изменение логина невозможно')
    
    @property
    def password(self):
        return self._password_hash
    
    @password.setter
    def password(self, value):
        self._password_hash = hash_function(value)


account = Account('hannymad', 'cakeisalie')
print(account.login)
print(account.password)

account = Account('timyr-guev', 'lovebeegeek')
print(account.password)
account.password = 'verylovebeegeek'
print(account.password)

account = Account('timyr-guev', 'lovebeegeek')
try:
    account.login = 'timyrik30'
except AttributeError as e:
    print(e)