import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilites.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = "//div[@class='cart-enter']"
    cart_page_title = "//span[text() = 'Ваша корзина,']"
    product_name_in_cart_1 = "(//a[@data-test-id='link__product-title'])[1]"
    product_name_in_cart_2 = "(//a[@data-test-id='link__product-title'])[2]"
    button_go_checkout = "//button[@data-test-id='button__go-checkout']"


    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_cart_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_page_title)))

    def get_product_name_in_cart_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name_in_cart_1)))

    def get_product_name_in_cart_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name_in_cart_2)))

    def get_button_go_checkout(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_go_checkout)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Клик кнопки корзины")
        time.sleep(10)

    def click_button_go_checkout(self):
        self.driver.execute_script("arguments[0].click();", self.get_button_go_checkout().click())
        print("Клик кнопки 'Перейти к оформлению'")


    # Metods

    def product_confirmation(self):
        Logger.add_start_step(method="product_confirmation")
        self.get_current_url()
        self.click_checkout_button()
        time.sleep(2)
        self.text_checking(self.get_cart_page_title(), 'Ваша корзина,')
        time.sleep(10)
        self.get_screenshot()
        self.click_button_go_checkout()
        Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")




