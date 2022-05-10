import os
import time
import pytest
from test_data import *
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def run_docker():
    os.system("docker run -d -p 4444:4444 -p 5900:5900 --shm-size=2g "
              "--name CRUD_for_user selenium/standalone-chrome-debug")
    time.sleep(4)


@pytest.fixture(autouse=True)
def driver(run_docker):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors=yes')

    driver = webdriver.Remote(
        command_executor=REMOTE_HOST,
        options=options
    )
    return driver


def find_by_xpath(driver, element):
    return driver.find_element(By.XPATH, element)

@pytest.fixture
def login(driver):
    driver.get(SITE_URL)
    username = find_by_xpath(driver, input_username)
    username.send_keys(ADMIN_LOGIN)
    password = find_by_xpath(driver, input_pass)
    password.send_keys(ADMIN_PASS)
    btn = find_by_xpath(driver, btn_login)
    btn.submit()






