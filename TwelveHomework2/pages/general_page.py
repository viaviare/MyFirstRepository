from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from supporting import Supporting


class GenaralPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.supporting = Supporting(self.driver)


    @property
    def input_name_product(self):
        return self.driver.find_element_by_css_selector("input[name='name[en]']")

    @property
    def input_code_product(self):
        return self.driver.find_element_by_css_selector("input[name='code']")

    @property
    def input_date_from(self):
        return self.driver.find_element_by_css_selector("input[name='date_valid_from']")

    @property
    def input_date_to(self):
        return self.driver.find_element_by_css_selector("input[name='date_valid_to']")

    @property
    def input_radio_but(self):
        return self.driver.find_element_by_css_selector("input[name='status']")


    def select_quantity_unit(self):
        Select(self.driver.find_element_by_css_selector("select[name = quantity_unit_id]")).select_by_visible_text("pcs")

    def select_delivery_status(self):
        Select(self.driver.find_element_by_css_selector("select[name = delivery_status_id]")).select_by_visible_text("3-5 days")

    def select_sold_out_status(self):
        Select(self.driver.find_element_by_css_selector("select[name = sold_out_status_id]")).select_by_visible_text("Sold out")


    def input_check_b(self):
        query = self.driver.find_element_by_css_selector("input[name='product_groups[]'][value ='1-3']")
        self.supporting.set_check_button(query)

    def input_check_b2(self):
        query = self.driver.find_element_by_css_selector("input[name='categories[]'][value ='1']")
        self.supporting.set_check_button(query)


    def upload_image(self):
        file_name = 'black_duck.jpg'
        file_dir = '/pics/'
        adap_name = self.supporting.path_adapt(file_dir,file_name)
        self.driver.find_element_by_css_selector("input[name='new_images[]']").send_keys(adap_name)

