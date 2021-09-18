## Frontend Project

# Pre-requisit
Before we can start launching this project with either Docker, Github Actions or Locally, it is required to download the latest chromedriver binary file.
Here is the link to the download page: https://chromedriver.chromium.org/downloads
Make sure that you download the correct binary file, that is: check your Chrome Browser version and make sure you are installing a chromedriver that supports it.

- Install chromedriver in your HOME directory
In order to make the process simplier, it is recommender to set the chromedriver binary into the HOME directory.

## Mac Version
If you owe a Mac, the steps are simple:

- Open your terminal
- Type echo $HOME so you can confirm what is your default directory 
- Move the chromedriver binary you have downloaded in the previous step to the $HOME directory

And then you should be able to launch the frontend automation tests
