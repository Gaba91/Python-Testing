Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given the user opens the login page
    When the user enters username "AndresGarcia"
    And the user enters password "123456789"
    And the user clicks on login button
    Then the user should see the home page


  Scenario: Login with invalid credentials
    Given the user opens the login page
    When the user enters username "JoseSosa01Bad"
    And the user enters password "PasswordBad"
    And the user clicks on login button
    Then the user should see an error message
    And the user should not see the home page