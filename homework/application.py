from selenium import webdriver
from pages.add_page import AddPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from supporting import Supporting

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()   #Chrome  Ie  Firefox
        self.main_page = MainPage(self.driver)
        self.add_page = AddPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.supporting = Supporting(self.driver)

    def quit(self):
        self.driver.quit()


    def add_items_in_cart(self):
        self.main_page.open()
        while True:
            self.main_page.choose_item_on_main_page.click()
            ic_next_var = self.add_page.var_quantity()

            self.add_page.present_element_select()
            self.add_page.add_item_button.click()
            self.add_page.wait_add_item_counter(ic_next_var)

            if int(self.add_page.var_quantity()) < 4:
                self.add_page.get_to_the_main_page.click()
            else:
                self.add_page.get_to_the_cart_page.click()
                break

    def remove_items_from_cart(self):
        self.supporting.implicit_wait()

        if len(self.cart_page.stop_moving_items)> 0:
            self.cart_page.stop_moving_items[0].click()

        list_buttons = self.cart_page.remove_buttons
        while len(list_buttons) > 0:
            goods_table = self.cart_page.remember_goods_table
            list_buttons[0].click()
            self.cart_page.wait_staleness_table(goods_table)
            list_buttons = self.cart_page.remove_buttons






