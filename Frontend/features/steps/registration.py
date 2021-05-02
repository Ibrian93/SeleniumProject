from behave import given, when, then
from Models.user import User
import features.steps.common


@given('the user goes to the Login Page')
def step_impl(context):
    context.login_page = context.main_page.go_to_login_page()

@given('the user goes to the New User Page')
def step_impl(context):
    context.registration_page = context.login_page.go_to_registration_page()

@given('the user introduces the following data')
def step_impl(context):
    for row in context.table:
        context.user = User(first_name=row["First Name"],
                            last_name=row["Last Name"],
                            user_name=row["UserName"],
                            password=row["Password"])
    context.registration_page.input_registration_form(first_name=context.user.first_name,
                                                      last_name=context.user.last_name,
                                                      username=context.user.user_name,
                                                      password=context.user.password)

@given('the user validates the recaptcha')
def step_impl(context):
    import time
    time.sleep(5)

@when('the user clicks on "Register"')
def step_impl(context):
    pass

@then('the user should be registered')
def step_impl(context):
    pass
