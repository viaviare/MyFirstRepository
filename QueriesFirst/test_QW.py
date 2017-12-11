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

#def catch_exceptions(query):
    #return len(driver.find_elements_by_css_selector(query)) > 0


def test_launch_query(driver):
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


    liElements = driver.find_elements_by_css_selector("li#app-")
    liNumbers = len(liElements)
    for i in range(liNumbers):
        liElements = driver.find_elements_by_css_selector("li#app-")
        liElements[i].click()
        #WebDriverWait(driver,20).until(EC.title_is("Help")) #проверить загрузку страницы ("My Store")
        #почему-то зависает и тест падает
            #?следует ли проверить главный список меню на наличие на новой странице
        liCurrents = driver.find_elements_by_xpath("//ul[@class='docs']/li")
        liInnerNum=len(liCurrents)
        if liInnerNum>0:
            for j in range(liInnerNum):
                liCurrents = driver.find_elements_by_xpath("//ul[@class='docs']/li")
                liCurrents[j].click()
                query = driver.find_elements_by_css_selector("h1")
        else:
            query = driver.find_elements_by_css_selector("h1") #не получается вызвать функцию catch_exceptions

        driver.get("http://localhost/litecart/admin")


