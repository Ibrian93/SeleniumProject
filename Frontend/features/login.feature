Feature: Login into the bookstore
	
	As a user 
	I want to be able to login into the bookstore
	So I can perform all my activities within the bookstore


	Scenario: A non logged user is able to login successfully into the bookstore
		Given the user is not logged into the bookstore main page
		And the user goes to the Login Page
		When the user attempts to login with its valid credentials
		Then the user should be logged in


	Scenario Outline: A non logged user attempts to login with invalid credentials
		Given the user is not logged into the bookstore main page
		And the user goes to the Login Page
		And the user has the following credentials:
			| username | password    |
			| ibrian93 | MyTesting83 |
		And the user introduces the username "<username>"
		And the user introduces the password "<password>"
		When the user attempts to login
		Then the login attempts fail with the following message "Invalid username or password!"
