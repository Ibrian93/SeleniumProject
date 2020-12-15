
class User(object):
    def __init__(self, id=None, username=None, firstname=None, lastname=None, email=None, password=None, phone=None, status=None):
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if status is not None:
            self.status = status
