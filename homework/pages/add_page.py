from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from supporting import Supporting


class AddPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.supporting = Supporting(self.driver)

    def var_quantity(self):
        ic_next_text = int(self.driver.find_element_by_css_selector("div#cart .quantity").text) + 1
        return ic_next_text

    @property
    def add_item_button(self):
        return self.driver.find_element_by_css_selector("button[name=add_cart_product]")

    def wait_add_item_counter(self, ic_next_text_from_var):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div#cart span.quantity"), str(ic_next_text_from_var)))

    @property
    def get_to_the_main_page(self):
        return self.driver.find_element_by_css_selector("li.general-0 a")

    @property
    def get_to_the_cart_page(self):
        return self.driver.find_element_by_css_selector("div#cart a.link")

    def present_element_select(self):
        if self.supporting.is_element_present(self.driver, By.CSS_SELECTOR, "select[name='options[Size]']") == True:  # element Select
            Select(self.driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_value("Small")
        return (self)
