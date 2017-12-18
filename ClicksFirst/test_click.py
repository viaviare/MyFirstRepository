import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver(request):
    webd=webdriver.Chrome()
    print(webd.capabilities)
    request.addfinalizer(webd.quit)
    return webd


def test_launch_query(driver):
    driver.get("http://localhost/litecart")
    #--------------------------
    link_reg = driver.find_element_by_css_selector("form[name=login_form] tbody a")
    link_reg.click()
    driver.find_element_by_css_selector("input[name=firstname]").send_keys("Maria_Merobella")
    driver.find_element_by_css_selector("input[name=lastname]").send_keys("Popins")
    driver.find_element_by_css_selector("input[name=email]").send_keys("Popins.Mari@gmail.com")
    driver.find_element_by_css_selector("input[name=postcode]").send_keys("98712")
    driver.find_element_by_css_selector("input[name=address1]").send_keys("6 Christian St, Rehoboth Beach")
    driver.find_element_by_css_selector("input[name=city]").send_keys("Rehoboth Beach")
#----------------------------- страна
    country_code=driver.find_element_by_css_selector("span[class=select2-selection__rendered]")
    ActionChains(driver).move_to_element(country_code).click().perform()
    search__field = driver.find_element_by_css_selector("input[class=select2-search__field]")
    ActionChains(driver).move_to_element(search__field).send_keys("United S").perform()
    ActionChains(driver).move_to_element(search__field).move_by_offset(20,40).click().perform()
    driver.find_element_by_css_selector("input[name=phone]").send_keys("+1") #удалялся код  (425)555-1212
#-----------------------------регион
    Select(driver.find_element_by_css_selector("select[name=zone_code]")).select_by_value("DE")
#-----------------------------пароль
    driver.find_element_by_css_selector("input[name=password]").send_keys("987654")
    driver.find_element_by_css_selector("input[name=confirmed_password]").send_keys("987654")
    driver.find_element_by_css_selector("button[name=create_account]").click()
#-----------------------------выход
    exit_link = driver.find_element_by_css_selector("div#box-account li:last-child a")
    ActionChains(driver).move_to_element(exit_link).click().perform()
#-----------------------------вход
    driver.find_element_by_css_selector("input[name=email]").send_keys("Popins.Mari@gmail.com")
    driver.find_element_by_css_selector("input[name=password]").send_keys("987654")
    driver.find_element_by_css_selector("button[name=login]").click()
    #-----------------------------выход
    exit_link = driver.find_element_by_css_selector("div#box-account li:last-child a")
    ActionChains(driver).move_to_element(exit_link).click().perform()