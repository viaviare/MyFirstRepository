import os
from selenium.webdriver.support.wait import WebDriverWait


class Supporting:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def path_adapt(self, file_dir, file_name):
        return os.path.join(os.path.dirname(__file__) + file_dir, file_name)


    def set_check_button(self, query):
        if query.get_attribute("checked") != "true":
            query.click()
        else:
            pass