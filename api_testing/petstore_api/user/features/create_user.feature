Feature: Create a user in the petstore api 

Scenario: A user can be created via API
    Given a user with the following data:
	    | username | firstname | lastname | email	   | password | phone      |
	    | brian    |  brian    | icochea  | test@test.com  | testing  | 123 456789 |
    And the user is active
    When it is created the user
    Then the user is created correctly

Scenario: A user is created and its information is retrieved correctly
    Given a user with the following data:
	    | username | firstname | lastname | email	   | password | phone      |
	    |  brian   |  brian    | icochea  | test@test.com  | testing  | 123 456789 |
    And the user is active
    And it is created the user
    When the user information is retrieved
    Then the information is retrieved correcly