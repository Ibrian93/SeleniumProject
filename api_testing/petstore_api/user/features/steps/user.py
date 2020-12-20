import requests
from api_testing.petstore_api.user.models.user_model import User
from behave import given, when, then


@given('a user with the following data')
def step_impl(context):
    for row in context.table:
        context.user = User(id=1, 
                            username=row["username"],
                            firstname=row["firstname"],
                            lastname=row["lastname"],
                            email=row["email"],
                            password=row["password"],
                            phone=row["phone"])
@given('the user is active')
def step_impl(context):
    context.user.status = 1

@when('it is created the user')
def step_impl(context):
    base_url = 'https://petstore.swagger.io/v2/'
    endpoint = 'user'
    header = {'accept': 'application/json', 'Content-type': 'application/json'}
    body = {'id': context.user.id,
            'username': context.user.username,
            'firstname': context.user.firstname,
            'lastname': context.user.lastname,
            'email': context.user.email,
            'password': context.user.password,
            'phone': context.user.phone,
            'userStatus': context.user.status}
    print(body)
    context.r = requests.post(base_url + endpoint, headers=header, data=body)

@then('the user is created correctly')
def step_impl(context):
    print(context.r.status_code)
    assert context.r.status_code == 200
