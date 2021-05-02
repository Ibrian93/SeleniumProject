from behave import given
from Pages.main_page import MainPage


@given('the user is not logged into the bookstore main page')
def step_impl(context):
    context.main_page = MainPage(context.driver)
    context.main_page.go_to_main_page()

