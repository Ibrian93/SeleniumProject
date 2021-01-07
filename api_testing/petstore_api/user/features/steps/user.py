import requests
import json
from api_testing.petstore_api.user.models.user_model import User
from api_testing.petstore_api.user.utils.constants import BASE_URL
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

@given('it is created the user')
@when('it is created the user')
def step_impl(context):
    endpoint = 'user'
    header = {'accept': 'application/json', 'Content-type': 'application/json'}
    context.body = {'id': context.user.id,
            'username': context.user.username,
            'firstname': context.user.firstname,
            'lastname': context.user.lastname,
            'email': context.user.email,
            'password': context.user.password,
            'phone': context.user.phone,
            'userStatus': context.user.status}
    context.r = requests.post(BASE_URL + endpoint, headers=header, data=json.dumps(context.body))

@when('the user information is retrieved')
def step_impl(context): 
    context.res = requests.get(BASE_URL + 'user/' + context.user.username)

@then('the information is retrieved correcly')
def step_impl(context):
    assert context.res.status_code == 200


@then('the user is created correctly')
def step_impl(context):
    assert context.r.status_code == 200

@then('the information retrieved matches with the created user')
def step_impl(context):
    response_info = context.res.text
    
    json_info = json.loads(response_info)
    for key in json_info:
        assert json_info[key] == context.body[key]
    