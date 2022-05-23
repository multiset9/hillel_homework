from conftest import browser
from test_data import *
from AdminPage import AdminPage


class TestSuiteCreateUser:
    def test_create_new_user(self, browser, login):
        create_user = AdminPage(browser)
        create_user.click_add_user_button()
        create_user.enter_username(USERNAME)
        create_user.enter_password(USERNAME_PASS, new_user_pass=True,
                                   confirm_pass=False)
        create_user.enter_password(USERNAME_PASS, new_user_pass=False,
                                   confirm_pass=True)
        create_user.click_save_button()
        actual_result = create_user.get_title_username()
        assert actual_result == USERNAME, f"User {USERNAME} wasn't created"
        create_user.log_out()

    def test_create_exists_user(self, browser, login):
        exists_user = AdminPage(browser)
        exists_user.click_add_user_button()
        exists_user.enter_username(USERNAME)
        exists_user.enter_password(USERNAME_PASS, new_user_pass=True,
                                   confirm_pass=False)
        exists_user.enter_password(USERNAME_PASS, new_user_pass=False,
                                   confirm_pass=True)
        exists_user.click_save_button()
        actual_result = exists_user.get_error_notification()
        assert actual_result == "A user with that username already exists."
        exists_user.log_out()

    def test_get_user(self, browser, login):
        get_user = AdminPage(browser)
        get_user.click_change_user_button()
        get_user.find_and_click_by_text()
        actual_result = get_user.get_title_username()
        assert actual_result == USERNAME
        get_user.log_out()

    def test_update_user(self, browser, login):
        update_user = AdminPage(browser)
        update_user.click_change_user_button()
        update_user.find_and_click_by_text()
        update_user.enter_first_last_name(FIRST_NAME, LAST_NAME)
        update_user.click_save_changes_user()
        actual_result = update_user.get_notification()
        assert actual_result == f"The user “{USERNAME}” was changed successfully."
        update_user.log_out()

    def test_delete_user(self, browser, login):
        delete_user = AdminPage(browser)
        delete_user.click_change_user_button()
        delete_user.find_and_click_by_text()
        delete_user.delete_user()
        actual_result = delete_user.get_notification()
        assert actual_result == f"The user “{USERNAME}” was deleted successfully."
















