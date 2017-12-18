import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver(request):
    webd=webdriver.Chrome()
    print(webd.capabilities)
    request.addfinalizer(webd.quit)
    return webd


def test_launch_query(driver):
    driver.get("http://localhost/litecart/admin")
    #--------------------------
    inputElement=driver.find_element_by_css_selector("input[name=username]")
    inputElement.send_keys("admin")
    inputElement=driver.find_element_by_css_selector("input[name=password]")
    inputElement.send_keys("admin")
    ButtonElement = driver.find_element_by_css_selector("button[name=login]")
    ButtonElement.click()
    WebDriverWait(driver,10).until(EC.title_is("My Store"))
    #--------------------------

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    countries_q = driver.find_elements_by_css_selector("tr.row")
    countries_list = list()

    for i in range(len(countries_q)):
        country_name = countries_q[i].find_element_by_xpath(".//td[5]").text
        countries_list.append(country_name)

        if countries_q[i].find_element_by_xpath(".//td[6]").text != "0":
            countries_q[i].find_element_by_css_selector("a").click()
            zones_list = list()
            zones_q = driver.find_elements_by_css_selector("table#table-zones tr")
            for j in range(1, len(zones_q) - 1):
                zone_name = zones_q[j].find_element_by_xpath(".//td[3]").text
                zones_list.append(zone_name)

            zones_list_sort = list(zones_list)
            zones_list_sort.sort()

            assert(zones_list_sort == zones_list)
            driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
            countries_q = driver.find_elements_by_css_selector("tr.row")

    countries_list_sort= list(countries_list)
    countries_list_sort.sort()
    assert(countries_list_sort == countries_list)

    #----------------------
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    countries_q = driver.find_elements_by_css_selector("tr.row")
    for i in range(len(countries_q)):
        countries_q[i].find_element_by_css_selector("a").click()
        zones_q = driver.find_elements_by_css_selector("table#table-zones tr")
        zones_list = list()

        for j in range(1, len(zones_q)):
            zones_in = zones_q[j].find_elements_by_xpath(".//td[3]/select/option")
            for t in range(len(zones_in)):
                if zones_in[t].get_attribute("selected")== "true":
                    zones_list.append(zones_in[t].text)
                    break

        zones_list_sort = list(zones_list)
        zones_list_sort.sort()

        assert(zones_list_sort == zones_list)
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        countries_q = driver.find_elements_by_css_selector("tr.row")
