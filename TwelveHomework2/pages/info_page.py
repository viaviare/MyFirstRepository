from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from supporting import Supporting


class InfoPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.supporting = Supporting(self.driver)


    @property
    def input_keywords(self):
        return self.driver.find_element_by_css_selector("input[name='keywords']")

    @property
    def input_short_descr(self):
        return self.driver.find_element_by_css_selector("input[name='short_description[en]']")

    @property
    def input_head_title(self):
        return self.driver.find_element_by_css_selector("input[name='head_title[en]']")

    @property
    def input_meta_descr(self):
        return self.driver.find_element_by_css_selector("input[name='meta_description[en]']")

    @property
    def put_full_descr(self):
        return self.driver.find_element_by_css_selector("div.trumbowyg-editor")

    def select_manufacturer_id(self):
        Select(self.driver.find_element_by_css_selector("select[name='manufacturer_id']")).select_by_visible_text("ACME Corp.")

