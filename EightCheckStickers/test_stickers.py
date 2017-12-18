import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wb = webdriver.Chrome()
    print(wb.capabilities)
    request.addfinalizer(wb.quit)
    return wb


def test_stickers(driver):
    driver.get("http://localhost/litecart")
    list_stickers = driver.find_elements_by_css_selector("li.product.column.shadow.hover-light")
    for i in range(len(list_stickers)):
        sticker = list_stickers[i].find_elements_by_css_selector("div.sticker")
        assert(len(sticker) == 1)


