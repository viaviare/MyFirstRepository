import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    webd = webdriver.Ie()  #Chrome  Firefox  Ie
    print(webd.capabilities)
    request.addfinalizer(webd.quit)
    return webd

def test_good_properties(driver):
    driver.get("http://localhost/litecart")

    item_name = driver.find_element_by_css_selector("div#box-campaigns div.name")
    old_price = driver.find_element_by_css_selector("div#box-campaigns .regular-price")
    dis_price = driver.find_element_by_css_selector("div#box-campaigns .campaign-price")
    #--------------------------font-size
    old_size = old_price.value_of_css_property("font-size")
    dis_size = dis_price.value_of_css_property("font-size")
    assert(old_size < dis_size)
    #--------------------------colors
    grey_color = old_price.value_of_css_property("color")
    red_color = dis_price.value_of_css_property("color")
    #-------------------------- grey
    pos_start =grey_color.find(chr(40))+ 1
    grey_color = grey_color[pos_start:len(grey_color)-1]
    grey_list = grey_color.split(", ")
    r_grey = int(grey_list[0])
    g_grey = int(grey_list[1])
    b_grey = int(grey_list[2])
    assert(r_grey == g_grey == b_grey)
    #-------------------------- red
    pos_start = red_color.find(chr(40))+ 1
    red_color = red_color[pos_start:len(red_color)-1]
    red_list = red_color.split(", ")
    g_red = int(red_list[1])
    b_red = int(red_list[2])
    assert(g_red == b_red == 0)
    #------------text vars
    item_name_text = item_name.text
    old_price_text = old_price.text
    dis_price_text = dis_price.text

    item_link = driver.find_element_by_css_selector("div#box-campaigns a.link").click()
    #----------- Wait
    WebDriverWait(driver,10).until(EC.presence_of_element_located("h1.title"))
    #----------- locators
    item_name_d = driver.find_element_by_css_selector("h1.title")
    old_price_d = driver.find_element_by_css_selector(".regular-price")
    dis_price_d = driver.find_element_by_css_selector(".campaign-price")
    #----------- s and strong (к сожалению, так и не придумала как это правильно прописать)
    old_price_s = driver.find_element_by_css_selector("s.regular-price")
    dis_price_strong = driver.find_element_by_css_selector("strong.campaign-price")
    #-----------
    assert(item_name_d.text == item_name_text) #names
    assert(old_price_d.text == old_price_text) #reg pricies
    assert(dis_price_d.text == dis_price_text) #dis pricies
    #-----font-size
    old_size_d = old_price_d.value_of_css_property("font-size")
    dis_size_d = dis_price_d.value_of_css_property("font-size")
    assert(old_size_d < dis_size_d)

