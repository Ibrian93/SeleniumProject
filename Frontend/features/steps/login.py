from behave import given, when, then
from Models.user import User
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import features.steps.common


@when('the user attempts to login with its valid credentials')
def step_impl(context):
    context.main_page = context.login_page.login_user_form("ibrian93", "MyTesting83!")


@then('the user should be logged in')
def step_impl(context):
    main_page_element_present = EC.presence_of_element_located((By.ID, context.main_page.username_field))
    WebDriverWait(context.driver, 3).until(main_page_element_present)
    assert 'ibrian93' in context.main_page.get_logged_username()
    assert 'Book Store' in context.main_page.get_title_page()
    assert 'books' in context.driver.current_url


@given('the user has the following credentials')
def step_impl(context):
    for row in context.table:
       context.user = User(user_name=row["username"], password=row["password"])


@given('the user introduces the username {username}')
def step_impl(context, username):
    context.login_page.set_username(username)


@given('the user introduces the password {password}')
def step_impl(context, password):
    context.login_page.set_password(password)


@when('the user attempts to login')
def step_impl(context):
    context.login_page.login_user()


@then('the login attempts fail with the following message "{message}"')
def step_impl(context, message):
    login_page_element_present = EC.presence_of_element_located((By.CSS_SELECTOR, context.login_page.error_message_field))
    WebDriverWait(context.driver, 3).until(login_page_element_present)
    assert message in context.login_page.get_error_message()

