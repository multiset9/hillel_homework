from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SITE_URL = "https://www.aqa.science/admin"


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = SITE_URL

    def find_element(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)
