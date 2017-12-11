import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    webd=webdriver.Chrome()
    print(webd.capabilities)
    request.addfinalizer(webd.quit)
    return webd

def catch_exceptions(query):
    return len(webdriver.find_elements_by_css_selector(query)) > 0


def test_launch_query(driver):
    driver.get("http://localhost/litecart/admin")
    ###########################
    inputElement=driver.find_element_by_css_selector("input[name=username]")
    inputElement.send_keys("admin")
    inputElement=driver.find_element_by_css_selector("input[name=password]")
    inputElement.send_keys("admin")
    ButtonElement = driver.find_element_by_css_selector("button[name=login]")
    ButtonElement.click()
    WebDriverWait(driver,10).until(EC.title_is("My Store")) #проверить загрузку страницы
#закрывает БР здесь
############################

def text_queries(catch_exceptions):
    query = driver.find_element_by_css_selector("ul.list-vertical")
    ulElement = driver.find_element_by_css_selector("ul.list-vertical")
    liElements = ulElement.find_elements_by_css_selector("ul li")
    #liNum = len(liElements)
    liNum = 0  #counter
    for element in liElements:
        liElements[liNum].click()
        WebDriverWait(driver,10).until(EC.title_is("Help")) #проверить загрузку страницы
        #?проверить главный список меню на наличие
        liCurrents = liElements[liNum].find_elements_by_css_selector("ul.docs")
        liInnerNum=len(ulCurrent)
        if liInnerNum>0:
            liInner = 0  #counter
            for element in liCurrents:
                liCurrents[liInner].click()
                query = driver.find_elements_by_css_selector("h1")
                liInner = liInner+1
        else:
            query = driver.find_elements_by_css_selector("h1")

        liNum=liNum+1
        driver.get("http://localhost/litecart/admin")



        #узнать порядковый номер элемента
        #найти по имени() список
        #и если больше 1
        # и в объекте организовать цикл
        #кликать и искать заголовки
        #проверить все ли меню прошёл
#def is_element_present()

