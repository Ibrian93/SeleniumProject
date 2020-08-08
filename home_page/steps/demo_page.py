from behave import given, when, then # pylint: disable=no-name-in-module
from selenium import webdriver


@given("the demo website")
def website_navigation(context):
    url = 'https://phptravels.com/demo/'
    context.browser = webdriver.Chrome('/home/ibrian93/chromedriver.exe')
    context.browser.get(url)


@given("the title is available in home")
def pass_function(context):
    pass
