class User:

    def __init__(self, first_name=None, last_name=None, user_name=None, password=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password

    @staticmethod
    def random_user():
        import random
        first_name = "brian"
        last_name = "testing"
        user_name = "ibrian" + str(random.randint(0, 1000))
        password = "testing+brian+" +str(random.randint(0, 1000))
        return User(first_name, last_name, user_name, password)

