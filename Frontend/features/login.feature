Feature: Login into the bookstore
	
	As a user 
	I want to be able to login into the bookstore
	So I can perform all my activities within the bookstore


	Scenario: A non logged user is able to login successfully into the bookstore
		Given the user is not logged into the bookstore main page
		And the user goes to the Login Page
		When the user attempts to login with its valid credentials
		Then the user should be logged in
		
