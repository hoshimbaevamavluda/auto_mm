import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilites.logger import Logger


class Main_page(Base):
    url = 'https://uzum.uz/ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.maximize_window()

    # Locators

    btn_catalog = "//div[@class='catalog-icon catalog-icon']"

    childrens_section = "(//span[text()='Детские товары'])[1]"
    toy_transports = "//a[@title='Игрушечный транспорт']"

    electronics_section = "//span[text()='Электроника']"
    eyepieces_section = "//a[@title='Окуляры']"

    # Getters
    def get_btn_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_catalog)))

    def get_childrens_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.childrens_section)))

    def get_toy_transports(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.toy_transports)))

    def get_electronics_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.electronics_section)))

    def get_eyepieces_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.eyepieces_section)))

    # Actions
    def click_btn_catalog(self):
        self.get_btn_catalog().click()
        print("Открытие каталога при клике")

    def click_childrens_section(self):
        self.hover_to_element(self.get_childrens_section())
        print("Наведение на 'Детские товары' для раскрытия подкатегорий")

    def click_toy_transports(self):
        self.get_toy_transports().click()
        print("Переход на страницу 'Игрушечный транспорт'")

    def click_electronics_section(self):
        self.hover_to_element(self.get_electronics_section())
        print("Наведение на 'Раздел электроники' для раскрытия подкатегорий")

    def click_eyepieces_section(self):
        self.get_eyepieces_section().click()
        print("Переход на страницу 'Окуляры'")

    # Metods
    def open_toys_page(self):
        Logger.add_start_step(method="open_toys_page")
        self.driver.get(self.url)
        self.get_current_url()
        time.sleep(5)
        self.click_btn_catalog()
        self.click_childrens_section()
        time.sleep(2)
        self.click_toy_transports()
        time.sleep(5)
        Logger.add_end_step(url=self.driver.current_url, method="open_toys_page")

    def open_eyepieces_page(self):
        Logger.add_start_step(method="open_eyepieces_page")
        self.click_btn_catalog()
        self.click_electronics_section()
        time.sleep(2)
        self.click_eyepieces_section()
        time.sleep(5)
        self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method="open_eyepieces_page")







