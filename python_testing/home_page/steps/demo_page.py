from behave import given, when, then # pylint: disable=no-name-in-module
from selenium import webdriver
from nose.tools import assert_equal


@given("the demo website")
def website_navigation(context):
    url = 'https://phptravels.com/demo/'
    context.browser = webdriver.Chrome()
    context.browser.get(url)
    import time
    time.sleep(10)

@given("the title is available in home")
def assert_title(context):
    title = context.browser.find_element_by_css_selector('h2.wow.fadeIn.upper.animated')
    assert_equal(title.text, 'APPLICATION TEST DRIVE')
