from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.common.by import By

import time
fearure_file = "../features/web_ui_crud_user.feature"
scenario_name = "Create New User"


@scenario(fearure_file, scenario_name)
def test():
    pass


@given(parsers.re("I go to the '(?P<add_user_url>.*)' page"))
def go_to_add_user_page(browser, login, add_user_url):
    browser.get(add_user_url)


@given(parsers.re("I enter '(?P<username>.*)' in the username field"))
def enter_username(browser, username):
    username_field = browser.find_element(
        By.XPATH, '//*[@id="id_username"]')
    username_field.click()
    username_field.send_keys(username)


@given(parsers.re("I enter '(?P<password>.*)' in the password field"))
def enter_password(browser, password):
    password_field = browser.find_element(By.XPATH, '//*[@id="id_password1"]')
    password_field.click()
    password_field.send_keys(password)


@given(parsers.re("I enter '(?P<password_confirm>.*)' in the password"
                  " confirmation field"))
def enter_password_confirm(browser, password_confirm):
    confirm_pass_field = browser.find_element(
        By.XPATH, '//*[@id="id_password2"]')
    confirm_pass_field.click()
    confirm_pass_field.send_keys(password_confirm)


@when("I click on the Save button")
def click_save_button(browser):
    save_button = browser.find_element(
        By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
    save_button.submit()
    if browser.find_element(
            By.XPATH,
            '//*[@id="user_form"]/div/fieldset/div[1]/ul/li').is_displayed():
        notification = browser.find_element(
            By.XPATH,
            '//*[@id="user_form"]/div/fieldset/div[1]/ul/li').text
        raise Exception(notification)


@then(parsers.re("'(?P<change_user>.*)' page is opened"))
def change_user_page(browser, change_user):
    title_page = browser.find_element(By.XPATH, '//*[@id="content"]/h1')
    actual_result = title_page.text
    assert actual_result == change_user


@then(parsers.re("The notification '(?P<notification>.*)'"
                  " is displayed at the top page"))
def notification_success(browser, notification):
    notification_success = browser.find_element(
        By.XPATH, '//*[@id="main"]/div/ul/li')
    actual_result = notification_success.text
    assert actual_result == notification
