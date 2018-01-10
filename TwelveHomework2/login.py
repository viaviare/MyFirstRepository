from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/admin")
        return self

    def is_on_this_page(self):
        return len(self.driver.find_elements_by_id("box-login")) > 0

    def authorization(self):
        self.driver.find_element_by_css_selector("input[name=username]").send_keys("admin")
        self.driver.find_element_by_css_selector("input[name=password]").send_keys("admin")
        self.driver.find_element_by_css_selector("button[name=login]").click()
        WebDriverWait(self.driver, 10).until(EC.title_is("My Store"))
