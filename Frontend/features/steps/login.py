from behave import given, when, then
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
