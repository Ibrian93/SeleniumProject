# Automation Portfolio
In this project you will find out my personal portfolio for test automation purposes.
Currently I am putting all my efforts to build a FE automation framework using the technologies described in the first point.


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

### How to run the tests?
You can chose weather you want to run them locally or dockers. My strongest suggestion is to run the automation tests in dockers. For that reason, the repository has all that it is required to run the tests so you have to only follow these steps:

- Clone the repository
- Assure you have the latest version installed
- cd into the Frontend folder
- run the following command `docker compose up --build --abort-on-container-exit`

And you will have the tests running in your local machine! Easy right? I am going to do a in-depth description about all the different steps and tools.


