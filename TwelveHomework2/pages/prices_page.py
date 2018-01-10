from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from supporting import Supporting


class PricesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.supporting = Supporting(self.driver)

    @property
    def input_purchase_price(self):
        return self.driver.find_element_by_css_selector("input[name='purchase_price']")

    @property
    def input_USD(self):
        return self.driver.find_element_by_css_selector("input[name='prices[USD]']")

    @property
    def input_EUR(self):
        return self.driver.find_element_by_css_selector("input[name='prices[EUR]']")

    def select_purchase_currency(self):
        Select(self.driver.find_element_by_css_selector("select[name='purchase_price_currency_code']")).select_by_visible_text("US Dollars")