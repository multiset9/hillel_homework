from BaseApp import BasePage
from selenium.webdriver.common.by import By


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
