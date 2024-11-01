import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.catalog_page import Catalog_page
from pages.main_page import Main_page


def test_buy_product_1(set_up, set_group):
    # очистка лишних записей в терминале с помощью options
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--headless")
    chrome_service = Service(
        executable_path='путь к файлу chromedriver.exe',
        chrome_options=options)
    driver = webdriver.Chrome(service=chrome_service)

    print("Start test1")

    mp = Main_page(driver)
    mp.open_birdhouses_page()
    mp.open_eyepieces_page()
    time.sleep(5)

    print("Test1 finish")
    driver.quit()


def test_buy_product_2(set_up, set_group):
    # очистка лишних записей в терминале с помощью options
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--headless")
    chrome_service = Service(
        executable_path='путь к файлу chromedriver.exe',
        chrome_options=options)
    driver = webdriver.Chrome(service=chrome_service)

    print("Start test2")

    mp = Main_page(driver)
    mp.open_birdhouses_page()

    cp = Catalog_page(driver)
    cp.item_to_cart_1()

    mp.open_eyepieces_page()

    cp.item_to_cart_2()

    crp = Cart_page(driver)
    crp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()
    time.sleep(5)

    print("Test_2 finish")
    driver.quit()

# def test_buy_product_3(set_up, set_group):
#     # очистка лишних записей в терминале с помощью options
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options.add_argument("--headless")
#     chrome_service = Service(
#         executable_path='C:\\Users\\admin\\Desktop\\QA\\автоматизация_тест\\resourse\\chrome\\chromedriver.exe',
#         chrome_options=options)
#     driver = webdriver.Chrome(service=chrome_service)
#
#     print("Start test")
#
#     mp = Main_page(driver)
#     mp.open_birdhouses_page()
#
#     cp = Catalog_page(driver)
#     cp.item_to_cart_1()
#
#     mp.open_eyepieces_page()
#
#     cp.item_to_cart_2()
#
#     crp = Cart_page(driver)
#     crp.product_confirmation()
#
#     cip = Client_information_page(driver)
#     cip.input_information()
#     time.sleep(5)
#
#     print("Test finish")
#     driver.quit()

# def test_buy_product_4(set_up, set_group):
#     # очистка лишних записей в терминале с помощью options
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options.add_argument("--headless")
#     chrome_service = Service(
#         executable_path='C:\\Users\\admin\\Desktop\\QA\\автоматизация_тест\\resourse\\chrome\\chromedriver.exe',
#         chrome_options=options)
#     driver = webdriver.Chrome(service=chrome_service)
#
#     print("Start test")
#
#     mp = Main_page(driver)
#     mp.open_birdhouses_page()
#
#     cp = Catalog_page(driver)
#     cp.item_to_cart_1()
#
#     mp.open_eyepieces_page()
#
#     cp.item_to_cart_2()
#
#     crp = Cart_page(driver)
#     crp.product_confirmation()
#
#     cip = Client_information_page(driver)
#     cip.input_information()
#     time.sleep(5)
#
#     print("Test finish")
#     driver.quit()
