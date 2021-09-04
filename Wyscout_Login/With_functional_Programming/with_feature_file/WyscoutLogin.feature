Feature: wyscout Login
  Scenario: Login to Wyscout with valid login credential
    Given  Launch Chrome Browser
    When open wyscout login page
    Then Enter User name and Password
    Then click on login button
