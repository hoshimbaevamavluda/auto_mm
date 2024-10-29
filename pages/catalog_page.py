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

    catalog_page_title = "//h1[@data-v-67d8a5b2]"

    # данные первого продукта
    filter_type_of_toy = "(//div[@class='filter-checkbox--label'])[1]"
    filter_color_red = "//div[normalize-space(text()) = 'Красный']"
    filter_brand = "//div[normalize-space(text()) = 'Amin Toys']"
    product_name_1 = "//a[normalize-space(text()) = 'Автомобиль Dakar']"
    select_product_1 = "//button[@title='Добавить Автомобиль Dakar в корзину']"

    filter_color_green = "//div[normalize-space(text()) = 'Зеленый']"
    product_name_2 = "//a[normalize-space(text()) = 'Монокль, бинокль для смартфона']"
    select_product_2 = "//button[@title='Добавить Монокль, бинокль для смартфона в корзину']"

    add_to_cart = "//div[normalize-space(text()) = 'Добавить в корзину']"



    # Getters

    def get_catalog_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_page_title)))

    def get_filter_type_of_toy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_type_of_toy)))

    def get_filter_color_red(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_color_red)))

    def get_filter_brand(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand)))

    def get_product_name_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name_1)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_filter_color_green(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_color_green)))

    def get_product_name_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name_2)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2)))



    # Actions

    def click_filter_type_of_toy(self):
        self.hover_and_click_to_element(self.get_filter_type_of_toy())
        print("Выбран фильтр игрушечного транспорта")

    def click_color_red(self):
        # Пример вызова функции для прокрутки к конкретному элементу
        self.hover_and_click_to_element(self.get_filter_color_red())
        print("Выбран фильтр - красный")

    def click_filter_brand(self):
        # Пример вызова функции для прокрутки к конкретному элементу
        self.hover_and_click_to_element(self.get_filter_brand())
        print("Выбран фильтр - бренда")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Клик на кнопку корзины товара")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Товар добавлен в корзину")

    def click_color_green(self):
        # Пример вызова функции для прокрутки к конкретному элементу и клика
        self.hover_and_click_to_element(self.get_filter_color_green())
        print("Выбран фильтр - зеленый")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        time.sleep(3)
        print("Клик на кнопку корзины в товаре")



    # Metods

    def use_filter_1(self):
        Logger.add_start_step(method="use_filter_1")
        self.text_checking(self.get_catalog_page_title(), 'Игрушечный транспорт')
        self.click_filter_type_of_toy()
        time.sleep(5)
        self.click_color_red()
        time.sleep(5)
        self.click_filter_brand()
        time.sleep(5)
        Logger.add_end_step(url=self.driver.current_url, method="use_filter_1")

    def select_products_1(self):
        Logger.add_start_step(method="select_products_1")
        self.get_current_url()
        self.click_select_product_1()
        time.sleep(2)
        self.click_add_to_cart()
        time.sleep(3)
        self.text_checking(self.get_product_name_1(), 'Автомобиль Dakar')
        Logger.add_end_step(url=self.driver.current_url, method="select_products_1")

    def use_filter_2(self):
        Logger.add_start_step(method="use_filter_2")
        self.text_checking(self.get_catalog_page_title(), 'Окуляры')
        self.click_color_green()
        Logger.add_end_step(url=self.driver.current_url, method="use_filter_2")

    def select_products_2(self):
        Logger.add_start_step(method="select_products_2")
        self.click_select_product_2()
        self.click_add_to_cart()
        self.text_checking(self.get_product_name_2(), 'Монокль, бинокль для смартфона')
        Logger.add_end_step(url=self.driver.current_url, method="select_products_2")
