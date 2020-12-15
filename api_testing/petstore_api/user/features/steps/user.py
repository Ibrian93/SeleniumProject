import requests
from api_testing.petstore_api.user.models.user_model import User
from behave import given, when, then


@given("a user with the following data:")
def step_impl(context):
    for row in context.table:
        context.user = User(id=1, 
                            username=row["username"],
                            firstname=row["firstname"],
                            lastname=row["lastname"],
                            email=row["email"],
                            password=row["password"],
                            phone=row["phone"])
