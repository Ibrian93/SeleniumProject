# API automation Project
This is a project where I show my API automation testing skills. 
The framework I have used for that purpose is `pytest`.
There are two ways to run the tests:

* Locally
* Via Dockers


## Run API tests locally :computer:
In order to run the tests locally make sure to follow these steps:
- Clone the repository 
- Make sure to pull the latest changes from origin
- Go to the `Backend` folder
- (optional) Create a virtual environment with the `python3 -m venv <folder_name>` command
- Install the requirements within the `requirements.txt`
- Launch the tests using the command `pytest Tests/`


## Run the tests via Dockers :whale: 

In order to run the tests via Dockers make sure to follow these steps:
- Clone the repository 
- Make sure to pull the latest changes from origin
- Install the latest version of [Dockers Desktop](https://www.docker.com/products/docker-desktop)
- Once installed if Dockers didn't start up automatically, do it manually
- Go to the `Backend` folder
- Here you will find a Dockerfile containing the instructions for the build of the image
- Execute the following command:
> Docker build -t <optional_tag_name>
- After the image has been build successfully, run the following command:
> Docker run -t <optional_tag_name>
