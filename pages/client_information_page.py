import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilites.logger import Logger


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    last_name = "//input[@name='lastname']"
    first_name = "//input[@name='firstname']"
    phone_number = "//input[@type='phone']"
    checkbox = "//span[@class='ke-checkbox--indicator']"


    # Getters
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox)))


    # Actions

    def input_first_name(self, first_name):
        self.input_text(self.get_first_name(), first_name, "имени")

    def input_last_name(self, last_name):
        self.input_text(self.get_last_name(), last_name, "фамилии")

    def input_phone_number(self, phone_number):
        self.hover_to_element(self.get_phone_number())
        self.input_text(self.get_phone_number(), phone_number, "номера телефона")

    def click_checkbox(self):
        self.hover_to_element(self.get_checkbox())
        self.get_checkbox().click()
        print("Клик чекбокса")

    # Metods
    def input_information(self):
        Logger.add_start_step(method="input_information")
        self.get_current_url()
        time.sleep(5)
        self.input_last_name("Ivanov")
        time.sleep(2)
        self.input_first_name("Ivan")
        time.sleep(2)
        self.input_phone_number("9565865468")
        time.sleep(2)
        self.click_checkbox()
        time.sleep(2)
        Logger.add_end_step(url=self.driver.current_url, method="input_information")


