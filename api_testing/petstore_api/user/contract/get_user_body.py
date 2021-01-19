from schema import Schema

user = Schema({'id': int,
                'username': str,
                'firstName': str,
                'lastName': str,
                'email': str,
                'password': str,
                'phone': str,
                'userStatus': int})