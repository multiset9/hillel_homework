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
        exists_user.enter_username(EXISTED_USERNAME)
        exists_user.enter_password(EXISTED_USERNAME_PASS, new_user_pass=True,
                                   confirm_pass=False)
        exists_user.enter_password(EXISTED_USERNAME_PASS, new_user_pass=False,
                                   confirm_pass=True)
        exists_user.click_save_button()
        actual_result = exists_user.get_error_notification()
        assert actual_result == "A user with that username already exists."
        exists_user.log_out()


