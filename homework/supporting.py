from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Supporting:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def is_element_present(self, driver, *args):
        try:
            self.driver.find_element(*args)
            return True
        except NoSuchElementException:
            return False


    def implicit_wait(self):
        self.driver.implicitly_wait(10)