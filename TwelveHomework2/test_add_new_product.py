from application import Application
from product import Product


def test_cart():
    app = Application()
    prod = Product()

    app.login_admin()
    app.catalog_page_button()
    app.fill_general_page(prod)
    app.fill_info_page(prod)
    app.fill_prices_page(prod)