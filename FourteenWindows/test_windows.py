import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.fixture
def driver(request):
    wd= webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_windows(driver):
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

    menu_list = driver.find_elements_by_css_selector("li#app- span.name")
    for i in range(len(menu_list)):
        if menu_list[i].text == "Countries":
            #menu_list[i].find_element_by_xpath("./../a").click() # не находит по родительской директории $x("//li[@id ='app-']//span[@class='name']/../a")
            liElements = driver.find_elements_by_css_selector("li#app- a")
            liElements[i].click()
            break
    driver.implicitly_wait(10)

    driver.find_element_by_css_selector("a.button").click()
    outer_list = driver.find_elements_by_css_selector("form[method=post] a[target = _blank]")
    for i in range(len(outer_list)):
        main_window = driver.current_window_handle
        window_list = driver.window_handles
        outer_list[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "head title")))
        new_window_list = driver.window_handles
        dif_windows = list(set(new_window_list) - set(window_list))
        driver.switch_to_window(dif_windows[0])
        driver.close()
        driver.switch_to_window(main_window)





