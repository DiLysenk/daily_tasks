from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from enum import Enum
from selenium import webdriver


class BasePage:

    def __init__(self, browser, wait=10):  # инициализация браузера
        self.browser = browser
        self.wait = WebDriverWait(self.browser, wait)


    def verify_link_text_visible(self, locator):
        """метод для верификации элемента в котором содержиться ссылка для перехода (за это отвечает аттрибут href=)
        для нахождения элемента достаточно указать название элемента"""
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise AssertionError(f'Не найти элемент с тексту -- {locator}')

    def click_element(self, element):
        return element.click()

    def enter_keys(self, element, text):
        return element.send_keys(text)



class HubDocker(BasePage, Enum):

    BTN_SING_UP = (By.CSS_SELECTOR, ".dbutton.styles__signUpButton___yf-Wn ")
    FIELD_FIND = (By.CSS_SELECTOR, ".autocompleteInput.styles__input___19pbM")


wd = webdriver.Chrome()
hb = HubDocker(wd)


