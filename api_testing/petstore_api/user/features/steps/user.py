import requests
from petstore_api.user.models import user_models
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
