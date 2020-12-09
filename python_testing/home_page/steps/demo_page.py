from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from nose.tools import assert_equal


@given("the demo website")
def website_navigation(context):
    url = 'https://phptravels.com/demo/'
    context.browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)
    context.browser.get(url)
    import time
    time.sleep(10)

@given("the title is available in home")
def assert_title(context):
    title = context.browser.find_element_by_css_selector('h2.wow.fadeIn.upper.animated')
    assert_equal(title.text, 'APPLICATION TEST DRIVE')
