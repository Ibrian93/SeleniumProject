# Frontend Project

## Purpose of this project
The main goal with this project is to propose an automation framework based on the following:
* Python
* BDD
* Docker

As we are working with Selenium, it is also implemented the [Page Object Pattern](https://www.selenium.dev/documentation/guidelines/page_object_models/)

In order to run the tests, you have two options:

## Run the tests locally
As in this project it is used the webdriver manager package, it is no longer required to download the chromedriver binary file. 
If you are still interested though, please feel free to check [here](https://chromedriver.chromium.org/downloads)

When inside the `Frontend` folder, execute the following command:
> `behave features/ -D driver=local`

Then you will have your tests running. Take into account that they are not running in headless mode, so a chrome window will spawn.


