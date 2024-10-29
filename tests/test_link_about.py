import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.main_page import Main_page


def test_link_about():
    # очистка лишних записей в терминале с помощью options
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_service = Service(executable_path='C:\\Users\\admin\\Desktop\\QA\\автоматизация_тест\\resourse\\chrome'
                                             '\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome(service=chrome_service)

    print("Start test")

    mp = Main_page(driver)
    mp.open_toys_page()

    cp = Catalog_page(driver)
    cp.use_filter_1()
    time.sleep(5)
    cp.select_products_1()

    # mp.open_eyepieces_page()
    #
    # cp.use_filter_2()
    # time.sleep(5)
    # cp.select_products_2()

    crp = Cart_page(driver)
    crp.product_confirmation()

    print("Test finish")
    driver.quit()
