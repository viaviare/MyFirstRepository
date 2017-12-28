import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wb = webdriver.Firefox()  #Chrome  Ie  Firefox
    print(wb.capabilities)
    request.addfinalizer(wb.quit)
    return wb


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


def test_add_cart(driver):
    driver.get("http://localhost/litecart")
    while True:
        driver.find_element_by_css_selector("div.content a.link").click()

        items_counter = driver.find_element_by_css_selector("div#cart .quantity")
        ic_next_text = int(items_counter.text)+1

        call_def = is_element_present(driver, By.CSS_SELECTOR, "select[name='options[Size]']") # element Select
        if call_def == True:
            Select(driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_value("Small")

        driver.find_element_by_css_selector("button[name=add_cart_product]").click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div#cart span.quantity"), str(ic_next_text)))

        if int(driver.find_element_by_css_selector("div#cart .quantity").text) < 3:
            driver.find_element_by_css_selector("li.general-0 a").click()
        else:
            driver.find_element_by_css_selector("div#cart a.link").click()
            break


    driver.implicitly_wait(10)
    small_icons = driver.find_elements_by_css_selector("a.inact")
    if len(small_icons)> 0:
        small_icons[0].click()

    buttons_r = driver.find_elements_by_css_selector("button[name = remove_cart_item]")
    while len(buttons_r) > 0:
        goods_table = driver.find_element_by_css_selector("table.dataTable.rounded-corners")
        buttons_r[0].click()
        WebDriverWait(driver, 10).until(EC.staleness_of(goods_table))
        buttons_r = driver.find_elements_by_css_selector("button[name = remove_cart_item]")


