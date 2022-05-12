from BaseApp import BasePage
from selenium.webdriver.common.by import By

from test_data import USERNAME


class AdminPagesLocators:
    """Admin page"""
    LOCATOR_INPUT_USERNAME = (By.XPATH, '//*[@id="id_username"]')
    LOCATOR_INPUT_PASS_ADMIN = (By.XPATH, '//*[@id="id_password"]')
    LOCATOR_INPUT_PASS_NEW_USER = (By.XPATH, '//*[@id="id_password1"]')
    LOCATOR_INPUT_PASS_NEW_USER_CONFIRM = (By.XPATH, '//*[@id="id_password2"]')
    LOCATOR_BTN_LOGIN = (By.XPATH, '//*[@id="login-form"]/div[3]/input')
    LOCATOR_BTN_ADD_USER = (
        By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a')
    LOCATOR_BTN_SAVE = (By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
    LOCATOR_TITLE_USERNAME = (By.XPATH, '//*[@id="content"]/h2')
    LOCATOR_NOTIFICATION_ERROR = (By.XPATH, '//*[@id="user_form"]/div/fieldset/div[1]/ul/li')
    LOCATOR_LOGOUT = (By.XPATH, '//*[@id="user-tools"]/a[3]')
    LOCATOR_LOGIN_AGAIN = (By.XPATH, '//*[@id="content"]/p[2]/a')
    LOCATOR_BTN_CHANGE_USER = (By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/td[2]/a')
    LOCATOR_USER_LINK = (By.LINK_TEXT, USERNAME)
    LOCATOR_INPUT_FIRST_NAME = (By.XPATH, '//*[@id="id_first_name"]')
    LOCATOR_INPUT_LAST_NAME = (By.XPATH, '//*[@id="id_last_name"]')
    LOCATOR_BTN_SAVE_CHANGE_USER = (By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
    LOCATOR_NOTIFICATION_SUCCESS = (By.XPATH, '//*[@id="main"]/div/ul/li')
    LOCATOR_BTN_DELETE_USER = (By.XPATH, '//*[@id="user_form"]/div/div/p/a')
    LOCATOR_BTN_DELETE_USER_APPROVED = (By.XPATH, '//*[@id="content"]/form/div/input[2]')



class AdminPage(BasePage):

    def enter_username(self, username):
        username_field = self.find_element(
            AdminPagesLocators.LOCATOR_INPUT_USERNAME)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def enter_password(self, password, new_user_pass=None, confirm_pass=None):
        if new_user_pass:
            password_field = self.find_element(AdminPagesLocators.
                                               LOCATOR_INPUT_PASS_NEW_USER)
        elif confirm_pass:
            password_field = self.find_element(
                AdminPagesLocators.LOCATOR_INPUT_PASS_NEW_USER_CONFIRM)
        else:
            password_field = self.find_element(
                AdminPagesLocators.LOCATOR_INPUT_PASS_ADMIN)
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element(AdminPagesLocators.LOCATOR_BTN_LOGIN)
        login_button.submit()

    def click_save_button(self):
        save_button = self.find_element(AdminPagesLocators.LOCATOR_BTN_SAVE)
        save_button.submit()

    def click_add_user_button(self):
        add_user_button = self.find_element(AdminPagesLocators.
                                            LOCATOR_BTN_ADD_USER)
        add_user_button.click()

    def click_change_user_button(self):
        change_user_button = self.find_element(AdminPagesLocators.LOCATOR_BTN_CHANGE_USER)
        change_user_button.click()

    def find_and_click_by_text(self):
        find_by_text = self.find_element(AdminPagesLocators.LOCATOR_USER_LINK)
        find_by_text.click()

    def get_title_username(self):
        title_username = self.find_element(
            AdminPagesLocators.LOCATOR_TITLE_USERNAME)
        return title_username.text

    def get_error_notification(self):
        notification = self.find_element(
            AdminPagesLocators.LOCATOR_NOTIFICATION_ERROR)
        return notification.text

    def log_out(self):
        logout_button = self.find_element(AdminPagesLocators.LOCATOR_LOGOUT)
        logout_button.click()
        login_again = self.find_element(AdminPagesLocators.LOCATOR_LOGIN_AGAIN)
        login_again.click()

    def enter_first_last_name(self, first_name, last_name):
        input_first_name = self.find_element(AdminPagesLocators.LOCATOR_INPUT_FIRST_NAME)
        input_first_name.click()
        input_first_name.send_keys(first_name)
        input_last_name = self.find_element(AdminPagesLocators.LOCATOR_INPUT_LAST_NAME)
        input_last_name.click()
        input_last_name.send_keys(last_name)

    def get_notification(self):
        notification = self.find_element(AdminPagesLocators.LOCATOR_NOTIFICATION_SUCCESS)
        return notification.text

    def click_save_changes_user(self):
        save = self.find_element(AdminPagesLocators.LOCATOR_BTN_SAVE_CHANGE_USER)
        save.click()

    def delete_user(self):
        delete_user = self.find_element(AdminPagesLocators.LOCATOR_BTN_DELETE_USER)
        delete_user.click()
        delete_user = self.find_element(AdminPagesLocators.LOCATOR_BTN_DELETE_USER_APPROVED)
        delete_user.click()
