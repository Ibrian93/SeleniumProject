from behave import given, when, then
import features.steps.common


@given('the user goes to the Login Page')
def step_impl(context):
    context.login_page = context.main_page.go_to_login_page()

@given('the user goes to the New User Page')
def step_impl(context):
    context.registration_page = context.login_page.go_to_registration_page()

@given('the user introduces the following data')
def step_impl(context):
    import time
    time.sleep(30)

@given('the user validates the recaptcha')
def step_impl(context):
    pass

@when('the user clicks on "Register"')
def step_impl(context):
    pass

@then('the user should be registered')
def step_impl(context):
    pass
