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

    first_name = "//input[@name='firstname']"
    last_name = "//input[@placeholder='Введите фамилию']"
    phone_number = "//input[@id='input-phone1240']"
    checkbox = "//span[@class='ke-checkbox--indicator']"


    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox)))


    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().click()
        self.get_first_name().send_keys(first_name)
        print("Ввод имени")
        time.sleep(2)

    def input_last_name(self, last_name):
        self.hover_to_element(self.get_last_name())
        self.get_last_name().send_keys(last_name)
        print("Ввод фамилии")
        time.sleep(2)

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Ввод номера телефона")
        time.sleep(2)

    def click_checkbox(self):
        self.get_checkbox().click()
        print("Клик чекбокса")
        time.sleep(2)

    # Metods
    def input_information(self):
        Logger.add_start_step(method="input_information")
        self.get_current_url()
        self.input_last_name("Ivanov")
        self.input_first_name("Ivan")
        self.input_phone_number("956586546")
        self.click_checkbox()
        Logger.add_end_step(url=self.driver.current_url, method="input_information")


