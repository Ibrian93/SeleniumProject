# Automation Portfolio
In this project you will find out my personal portfolio for test automation purposes.
Here I have 2 main project:
- Web Automation
- API automation

## 1. Web Automation:
For the web automation I use the following tecnologies:
- Behave
- Selenium
- Python

### Behave 
[Behave](https://behave.readthedocs.io/en/latest/) is a python framework for automation testing that allows the QA team to implement BDD within the scripts.


### Selenium
[Selenium](https://www.selenium.dev/) Selenium (Webdriver) is the main automation tool for testers which allows the interaction with the web. It has several usages but it main goal is the web automation. 

### Python
As I am using Behave, which is an automation Framework, I use python as my main programming language.

### Web under automation
https://phptravels.com/demo/ is the main page under test.


## 2. API Automation:
For the API automation I use:
- Behave
- Request
- Python

### Why Behave for API testing
Why do I use behave for API testing? I strongly believe that it is important to address all our tests cases to everyone, so that understand the product under testing as well as its behavior. 

### Request
Request is the main library for api calls integrated with python.

### API under automation 
https://petstore.swagger.io/ is the swagger for the API testing


# How to run the automated tests?
## Web Test automation
To run it, you simply need to run the command behave followed by the route of the location of the feature file.

That is: 
```
behave python_testing/home_page/demo_page.feature
```

## Api automation test
In order to run the tests, the project path must be added to the PYTHONPATH. 
Open your `.bashrc` and add the following config
```
PYTHONPATH={path_to_the_project}/selenium_project/api_testing:$PYTHONPATH
export PYTHONPATH
```
that will allow us to add the project to the system environment variables so Python could load all the modules. (It is recommended to reboot your computer)

Once this step has been completed, go to the `selenium_project` folder and launch the tests with the following command
```
behave api_testing/petstore_api/user/features/create_user.feature
```