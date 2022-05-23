import os
import time
import pytest
from test_data import *
from selenium import webdriver
from AdminPage import AdminPage

REMOTE_HOST = "http://localhost:4444/wd/hub"


@pytest.fixture(scope="session")
def run_docker():
    os.system("docker run -d -p 4444:4444 -p 5900:5900 --shm-size=2g "
              "--name CRUD_for_user selenium/standalone-chrome-debug")
    time.sleep(4)
    yield
    os.system("docker stop CRUD_for_user")
    os.system("docker rm /CRUD_for_user")


@pytest.fixture(scope="session")
def browser(run_docker):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors=yes')

    driver = webdriver.Remote(
        command_executor=REMOTE_HOST,
        options=options
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_site()
    admin_page.enter_username(ADMIN_USERNAME)
    admin_page.enter_password(ADMIN_PASS)
    admin_page.click_login_button()






