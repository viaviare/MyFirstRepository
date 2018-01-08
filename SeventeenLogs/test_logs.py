import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver(request):
    caps = DesiredCapabilities.CHROME
    caps['loggingPrefs'] = {'browser': 'ALL'}
    wd= webdriver.Chrome(desired_capabilities=caps)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_goods_pages_logs(driver):
    driver.get("http://localhost/litecart/admin")
    #--------------------------
    inputElement=driver.find_element_by_css_selector("input[name=username]")
    inputElement.send_keys("admin")
    inputElement=driver.find_element_by_css_selector("input[name=password]")
    inputElement.send_keys("admin")
    ButtonElement = driver.find_element_by_css_selector("button[name=login]")
    ButtonElement.click()
    WebDriverWait(driver,10).until(EC.title_is("My Store")) #проверить загрузку страницы
    #--------------------------

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    tdElements = driver.find_elements_by_css_selector("tr.row td:nth-of-type(3) a")
    tdNumbers = len(tdElements)

# критично ли не кликать по папкам (только товары)?
    for i in range(tdNumbers):
        tdElements[i].click()
        print(driver.log_types)
        print(driver.get_log("browser"))

        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        tdElements = driver.find_elements_by_css_selector("tr.row td:nth-of-type(3) a")