
Feature: CRUD for user profile API

  Background:
    Given I log in as 'admin' with 'admin123' on the 'https://www.aqa.science' resource

  @apitest
  Scenario Outline: Create new user
    Given I set '/users/' api endpoint
    When I send POST HTTP request with '<payload>' and '<uniq_id>'
    Then I receive valid HTTP response code '201'
    Then I receive valid HTTP response with '<payload>'
    Examples:
      | payload                                                    |uniq_id|
      | '{"username": "Jon_Jones", "email": "jon_jones@gmail.com", "group": []}' |1|
      | '{"username": "Jon_Jones34", "email": "jon_jones23@gmail.com", "group": []}' |2|

  @apitest
  Scenario Outline: Get created user
    When I send GET HTTP request to unique user endpoint '<uniq_id>'
    Then I receive valid HTTP response code '200'
    Then I receive valid HTTP response with '<payload>'
    Examples:
      | payload                                                      |uniq_id|
      | '{"username": "Jon_Jones", "email": "jon_jones@gmail.com", "group": []}' |1|
      | '{"username": "Jon_Jones34", "email": "jon_jones23@gmail.com", "group": []}' |2|

  @apitest
  Scenario Outline: Update created user
    When I send PUT HTTP request with '<payload>' to unique user endpoint '<uniq_id>'
    Then I receive valid HTTP response code '200'
    Then I receive valid HTTP response with '<payload>'
    Examples:
      | payload                                                      |uniq_id|
      | '{"username": "Jon_Richard", "email": "jon_richard@gmail.com"}' |1|
      | '{"username": "Jon_Rich", "email": "rich@gmail.com"}' |2|

  @apitest
  Scenario Outline: Delete user
    When I send DELETE HTTP request to unique user endpoint '<uniq_id>'
    Then I receive valid HTTP response code '204'
    Examples:
    |uniq_id|
    |       1|
    |        2|
