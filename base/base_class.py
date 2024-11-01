import datetime
import time

from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver


    '''Метод возврата URL'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    '''Метод проверки слов'''

    @staticmethod
    def text_checking(word, result):
        value_word = word.text
        assert value_word == result, 'Данные не соответствуют'
        print("Данные идентичны:" + value_word)

    '''Метод Screenshot'''

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('путь к файлу\\screen\\' + name_screenshot)

    '''Метод проверки URL'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

    '''Метод навигации на элемент'''

    def hover_to_element(self, element):
        try:
            # Прокручиваем элемент в зону видимости
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

            # Наведение на элемент с использованием ActionChains
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print(f"Наведение после прокрутки на: {element.text}")
            time.sleep(3)

        except Exception as e:
            print(f"Произошла ошибка при наведении на: {e}")

    '''Метод для ввода текста'''
    def input_text(self, element, text, field_name=""):
        try:
            element.click()
            element.send_keys(text)
            print(f"Ввод {field_name} успешно выполнен")
        except Exception as e:
            print(f"Ошибка при вводе {field_name}: {e}")

