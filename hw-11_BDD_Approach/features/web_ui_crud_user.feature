
Feature: CRUD for user profile

Scenario: Create New User
  Given I go to the 'https://www.aqa.science/admin/auth/user/add/' page
  And I enter 'Jon54' in the username field
  And I enter 'Qwer1234!' in the password field
  And I enter 'Qwer1234!' in the password confirmation field
  When I click on the Save button
  Then 'Change user' page is opened
  Then The notification 'The user “Jon54” was added successfully. You may edit it again below.' is displayed at the top page