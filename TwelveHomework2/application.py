from selenium import webdriver
from pages.general_page import GenaralPage
from pages.info_page import InfoPage
from pages.prices_page import PricesPage
from pages.catalog_page import CatalogPage
from supporting import Supporting
from login import Login
from product import Product

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()   #Chrome  Ie  Firefox
        self.catalog_page = CatalogPage(self.driver)
        self.general_page = GenaralPage(self.driver)
        self.info_page = InfoPage(self.driver)
        self.prices_page = PricesPage(self.driver)
        self.login = Login(self.driver)
        self.product = Product(self)
        self.supporting = Supporting(self.driver)

    def quit(self):
        self.driver.quit()

    def login_admin(self):
        if self.login.open().is_on_this_page():
            self.login.authorization()
            return self.catalog_page.open()

    def catalog_page_button(self):
        self.catalog_page.new_product_button()

    def fill_general_page(self, product):
        self.general_page.input_name_product.send_keys(product.product_name)
        self.general_page.input_code_product.send_keys(product.product_code)
        self.general_page.input_date_from.send_keys(product.date_from)
        self.general_page.input_date_to.send_keys(product.date_to)
        self.general_page.select_quantity_unit()
        self.general_page.select_delivery_status()
        self.general_page.select_sold_out_status()
        self.general_page.upload_image()
        self.general_page.input_radio_but.click()
        self.general_page.input_check_b()
        self.general_page.input_check_b2()


    def fill_info_page(self, product):
        self.catalog_page.click_info_part.click()
        self.info_page.input_head_title.send_keys(product.head_title)
        self.info_page.input_keywords.send_keys(product.keywords)
        self.info_page.input_short_descr.send_keys(product.short_desc)
        self.info_page.input_meta_descr.send_keys(product.meta_desc)
        self.info_page.select_manufacturer_id()
        self.info_page.put_full_descr.send_keys(product.full_desc)



    def fill_prices_page(self, product):
        self.catalog_page.click_prices_part.click()
        self.prices_page.input_purchase_price.clear()
        self.prices_page.input_purchase_price.send_keys(product.purchase_price)
        self.prices_page.input_USD.send_keys(product.prices_USD)
        self.prices_page.input_EUR.send_keys(product.prices_EUR)
        self.prices_page.select_purchase_currency()
        self.catalog_page.click_save_button.click()