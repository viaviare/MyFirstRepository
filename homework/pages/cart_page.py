from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def stop_moving_items(self):
        return self.driver.find_elements_by_css_selector("a.inact")

    @property
    def remove_buttons(self):
        return self.driver.find_elements_by_css_selector("button[name = remove_cart_item]")

    @property
    def remember_goods_table(self):
        return self.driver.find_element_by_css_selector("table.dataTable.rounded-corners")

    def wait_staleness_table(self, goods_table):
        WebDriverWait(self.driver, 10).until(EC.staleness_of(goods_table))
