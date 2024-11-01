import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilites.logger import Logger


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    catalog_page_title = "//h1[@data-test-id='text__title']"

    filter_brand = "//div[normalize-space(text()) = 'Triol']"
    product_name_1 = "//h1[@data-test-id='text__title']"
    add_to_cart_1 = "//button[@data-test-id='button__add-to-cart']"

    product_name_2 = "(//a[@data-test-id='text__product-name'])[2]"
    add_to_cart_2 = "(//button[@data-test-id='button__add-to-cart'])[2]"



    # Getters

    def get_catalog_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_page_title)))

    def get_filter_brand(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand)))

    def get_product_name_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name_1)))

    def get_add_to_cart_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_1)))

    def get_product_name_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name_2)))

    def get_add_to_cart_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_2)))


    # Actions
    def click_add_to_cart_1(self):
        self.get_add_to_cart_1().click()
        print(f"{self.get_product_name_1()} добавлен в корзину")

    def click_add_to_cart_2(self):
        self.get_add_to_cart_2().click()
        print(f"{self.get_product_name_1()} добавлен в корзину")

    def click_filter_brand(self):
        self.get_filter_brand().click()
        print("Выбран фильтр бренда")



    # Metods

    def item_to_cart_1(self):
        Logger.add_start_step(method="item_to_cart_1")
        time.sleep(5)
        self.text_checking(self.get_catalog_page_title(), 'Скворечники и гнезда для птиц')
        time.sleep(5)
        self.click_filter_brand()
        time.sleep(5)
        self.click_add_to_cart_1()
        time.sleep(5)
        Logger.add_end_step(url=self.driver.current_url, method="item_to_cart_1")

    def item_to_cart_2(self):
        Logger.add_start_step(method="item_to_cart_2")
        self.text_checking(self.get_catalog_page_title(), 'Окуляры для оптических приборов')
        time.sleep(5)
        self.click_add_to_cart_2()
        time.sleep(5)
        Logger.add_end_step(url=self.driver.current_url, method="item_to_cart_2")
