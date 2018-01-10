from selenium.webdriver.support.wait import WebDriverWait


class CatalogPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        return self

    def new_product_button(self):
        aButtons = self.driver.find_elements_by_css_selector("a.button")
        for i in range(len(aButtons)):
            if aButtons[i].text == "Add New Product":
                aButtons[i].click()
                break

    @property
    def click_info_part(self):
        return self.driver.find_element_by_css_selector("ul.index li:nth-of-type(2)")

    @property
    def click_prices_part(self):
        return self.driver.find_element_by_css_selector("ul.index li:nth-of-type(4)")

    @property
    def click_save_button(self):
        return self.driver.find_element_by_css_selector("button[name='save']")
