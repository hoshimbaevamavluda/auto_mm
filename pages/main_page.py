import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilites.logger import Logger


class Main_page(Base):
    url = 'https://mm.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.maximize_window()

    # Locators
    closing_advertising = "//div[@class='close']"

    btn_catalog = "//div[@class='button-catalog']"

    pet_supplies_section = "//span[text()='Зоотовары']"
    birdhouses_for_birds = "//a[@title='Скворечники и гнезда']"

    electronics_section = "//span[text()='Электроника']"
    eyepieces_section = "//a[@title='Окуляры']"

    # Getters
    def get_closing_advertising(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.closing_advertising)))

    def get_btn_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_catalog)))

    def get_pet_supplies_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.pet_supplies_section)))

    def get_birdhouses_for_birds(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.birdhouses_for_birds)))

    def get_electronics_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.electronics_section)))

    def get_eyepieces_section(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.eyepieces_section)))

    # Actions
    def click_closing_advertising(self):
        self.get_closing_advertising().click()
        print("Убрать рекламу")

    def click_btn_catalog(self):
        self.get_btn_catalog().click()
        print("Открытие каталога при клике")

    def click_pet_supplies_section(self):
        self.hover_to_element(self.get_pet_supplies_section())

    def click_birdhouses_for_birds(self):
        self.get_birdhouses_for_birds().click()
        print("Переход на страницу 'Скворечники и гнезда'")

    def click_electronics_section(self):
        self.hover_to_element(self.get_electronics_section())

    def click_eyepieces_section(self):
        self.hover_to_element(self.get_eyepieces_section())
        self.get_eyepieces_section().click()
        print("Переход на страницу 'Окуляры'")


    # Metods

    def open_birdhouses_page(self):
        Logger.add_start_step(method="open_birdhouses_page")
        self.driver.get(self.url)
        self.get_current_url()
        self.click_closing_advertising()
        time.sleep(3)
        self.click_btn_catalog()
        time.sleep(2)
        self.click_pet_supplies_section()
        time.sleep(3)
        self.click_birdhouses_for_birds()
        time.sleep(5)
        self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method="open_birdhouses_page")

    def open_eyepieces_page(self):
        Logger.add_start_step(method="open_eyepieces_page")
        self.click_btn_catalog()
        self.click_electronics_section()
        time.sleep(2)
        self.click_eyepieces_section()
        time.sleep(5)
        self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method="open_eyepieces_page")







