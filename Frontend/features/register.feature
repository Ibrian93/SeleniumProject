Feature: Register into the Bookstore

	As a user
	I want to be able to register into the bookstore
	So I can record all my activities within the company

	@skip
	Scenario: A user register succesfully into the bookstore
		Given the user is not logged into the bookstore main page
		And the user goes to the Login Page
		And the user goes to the New User Page
		And the user introduces the following data:
		    | First Name | Last Name | UserName | Password  |
			|  Testing   |   Test    | TestingT | Testing00!|
		And the user validates the recaptcha
		When the user clicks on "Register"
		Then the user should be registered

