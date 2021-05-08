from behave import fixture, use_fixture
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from Models.user import User
from behave.log_capture import capture
import os
import time

# USE: behave -D BEHAVE_DEBUG_ON_ERROR     (to enable debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes (to enable debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no  (to disable degug-on-error)


BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)
    context.artifacts_dir = 'artifacts'
    context.config.setup_logging()


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    if "generate_user" in scenario.effective_tags:
        context.user = User.random_user()
    if context.config.userdata["driver"] == "remote":
        use_fixture(driver_remote, context)
    else:
        use_fixture(driver_local, context)

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)

@capture
def after_scenario(context, scenario):
    #take screenshot if scenario fails
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join(context.artifacts_dir, 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.png')
        context.driver.save_screenshot(scenario_file_path)

def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)


@fixture
def driver_local(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    yield
    context.driver.quit()


@fixture
def driver_remote(context):
    context.driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
    yield
    context.driver.quit()
