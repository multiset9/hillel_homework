from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

REMOTE_HOST = "http://localhost:4444/wd/hub"
SITE_URL = "https://influencermarketinghub.com/instagram-money-calculator/"
username_field = '//*[@id="channel"]/input'
test_data = ["test"]
created_block = '//*[@id="twitter-calc"]/div/div[2]/div[1]/div[2]/div[3]'


def create_docker_container():
    os.system("docker run -d -p 4444:4444 -p 5900:5900 --shm-size=2g "
              "--name first_web-test_chrome selenium/standalone-chrome-debug")
    time.sleep(4)


def remove_docker_container():
    os.system("docker stop first_web-test_chrome")
    os.system("docker rm /first_web-test_chrome")


create_docker_container()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors=yes')

driver = webdriver.Remote(
    command_executor=REMOTE_HOST,
    options=options
)

driver.get(SITE_URL)
element = driver.find_element(By.XPATH, username_field)
element.send_keys(test_data[0])
element.submit()
expected_element = driver.find_element(By.XPATH, created_block)
time.sleep(4)
assert expected_element.text == "64,278"

remove_docker_container()






