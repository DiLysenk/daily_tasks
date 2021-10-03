# -*- coding: utf-8 -*-
import logging
import time
from time import sleep
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
CLICK_RETRY = 5

class BasePage:  # базовый класс для PageObject

    LOADING_TAG = (By.CSS_SELECTOR, '.-loading.-active')  # селектор элемента загрузки
    MENU_LINK_TO_CONTENT_PAGE = (By.CSS_SELECTOR, '[href="/new/shows"]')  # кнопка видна из всех разделов



    def __init__(self, browser, wait=10):  # инициализация браузера
        self.browser = browser
        self.wait = WebDriverWait(self.browser, wait)
        self.logger = logging.getLogger(type(self).__name__)

    def is_page_loaded(self):
        self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
        self.is_not_visible(self.LOADING_TAG)
        self.is_not_visible((By.XPATH, "//div[contains(@class, 'loading -active')]"))


    def is_selected(self, element):
        """метод для проверки -выделен ли элемент? на странице  """
        if 'selected' not in element.get_attribute("class"):
            raise AssertionError("ошибка, элемент не был выделен в таблице ")

    def is_visible_by_link_text(self, text):
        """метод для верификации элемента в котором содержиться ссылка для перехода (за это отвечает аттрибут href=)
        для нахождения элемента достаточно указать название элемента"""
        try:
            self.is_page_loaded()
            element = self.wait.until(ec.visibility_of_element_located((By.LINK_TEXT, text)))
            self.logger.info(f'успешно найден элемент с текстом -- {text}')
            return element
        except TimeoutException:
            self.logger.error(f'Ошибка, не найдена ссылка с текстом "{text}')
            raise AssertionError(f'Ошибка, не найдена ссылка с текстом "{text}')

    def is_visible(self, locator: tuple):
        """метод для верификации "видимого" элемента на странице с помощью селектора"""
        try:
            self.is_page_loaded()
            element = self.wait.until(ec.visibility_of_element_located(locator))
            self.logger.info(f'успешно найден элемент по локатору с локатором {locator}')
            return element
        except TimeoutException:
            self.logger.error(f'ошибка, не найден элемент по css {locator}')
            raise AssertionError(f'ошибка, не найден элемент по css  {locator}')

    def is_presence(self, locator: tuple):
        """метод для верификации элемента на странице с помощью селектора
        (элемент может быть невидим на странице но он присутствует в DOM)"""
        try:
            self.is_page_loaded()
            element = self.wait.until(ec.presence_of_element_located(locator))
            self.logger.info(f'успешно найден элемент по локатору с локатором {locator}')
            return element
        except TimeoutException:
            self.logger.error(f'ошибка, не найден элемент по css  {locator}')
            raise AssertionError(f'ошибка,не найден элемент по css  {locator}')

    def is_visible_by_text(self, text: str):
        """метод для верификации элемента по его названию ,
        для нахождения элемента достаточно указать название элемента"""
        try:
            self.is_page_loaded()
            element = self.wait.until(ec.visibility_of_element_located((By.XPATH, f'//*[text()="{text}"]')))
            self.logger.info(f'найден элемент с текстом {text}')
            return element
        except TimeoutException:
            self.logger.error(f'Ошибка,  не найден элемент с названием {text}')
            raise AssertionError(f'Ошибка, не найден элемент с названием {text}')

    # метод для верификации элементов с помощью локатора
    def are_visible(self, locator: tuple, quantity: int = 1):
        """метод для верификации элементОВ по селектору,
        quantity: это предпологаемое минимальное количество которое он должен найти"""
        try:
            self.is_page_loaded()
            if len(self.wait.until(ec.visibility_of_all_elements_located(locator))) >= quantity:
                return self.wait.until(ec.visibility_of_all_elements_located(locator))
            else:
                self.wait_time(3)
                return self.wait.until(ec.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f'Ошибка, элемент не найден {locator}')
            raise AssertionError(f'Ошибка, элемент не найден {locator}')


    def are_presence(self, locator: tuple, quantity: int = 1):
        """метод для верификации элементОВ по селектору,
        quantity: это предпологаемое минимальное количество которое он должен найти"""
        try:
            self.is_page_loaded()
            if len(self.wait.until(ec.presence_of_all_elements_located(locator))) >= quantity:
                return self.wait.until(ec.presence_of_all_elements_located(locator))
            else:
                self.wait_time(3)
                return self.wait.until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f'Ошибка, элемент не найден {locator}')
            raise AssertionError(f'Ошибка, элемент не найден {locator}')

    def is_clickable(self, locator: tuple):
        """метод для верификации элемента с помощью CSS на кликабельность"""
        try:
            self.is_page_loaded()
            element = self.wait.until(ec.element_to_be_clickable(locator))
            self.logger.info(f'найден кликабельный элемент {locator}')
            return element
        except TimeoutException:
            self.logger.error(f'Ошибка, элемент не кликабельный {locator}')
            raise AssertionError(f'Ошибка, элемент не кликабельный {locator}')

    def is_not_visible(self, locator: tuple):
        try:
            return self.wait.until(ec.invisibility_of_element(locator))
        except TimeoutException:
            self.logger.error(f'Ошибка, элемент найден и не исчезает {locator}')
            raise AssertionError(f'Ошибка, элемент не исчез с экрана {locator}')

    def verify_url(self, url):
        try:
            return self.wait.until(ec.url_to_be(url))
        except TimeoutException:
            self.logger.error(f'Ошибка, адрес странички не  {url}')
            raise AssertionError(f'Ошибка, адрес странички не  {url}')

    def click_element_ac(self, element):
        """клик с помощью экшон чейнс"""
        ActionChains(self.browser).pause(0.1).move_to_element(element).click().perform()

    def click_element(self, element):
        for i in range(CLICK_RETRY):
            try:
                self.is_page_loaded()
                element.is_enabled()
                element.click()
                self.logger.info('клик по элементу')
                time.sleep(i)
                break
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise AssertionError(f'Ошибка, не кликнуть по элементу через {i} сек')




    def click_locator(self, locator):
        for i in range(CLICK_RETRY):
            try:
                element = self.is_presence(locator)
                self.scroll_to_element(element)
                element = self.wait.until(ec.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def click_nth_child(self, element, locator: tuple, index: int = 0):
        """ в найденом элементе (например таблице) находит элементы с одинаковым css_selector
         и кликает по порядковому номеру (index) """
        element_child = element.find_elements(*locator)[index]
        self.click_element(element_child)
        self.logger.info(f'Клик в элемент по счёту {index} с локатором {locator}')
        return self

    def clear_and_send_keys(self, element, text):
        """ввод в поле текста, после очистки его """
        element.clear()
        element.send_keys(text)
        self.logger.info(f'заполняем поле текстом -- {text}')
        return self

    def send_keys_with_enter(self, element, text):
        """ввод в поле текста и последующее нажатие ENTER
        Подходит для полей фильтров с выпадающем списком"""
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
        self.logger.info(f'заполняем поле текстом -- {text} и нажимаем Enter')
        return self

    def get_attribute_element(self, element, attribute):
        return element.get_attribute(attribute)

    # sleep сделан для того что бы не было разлогиневания
    def refresh_browser(self):
        self.wait_time(1)
        self.browser.refresh()
        self.is_page_loaded()
        self.wait_time(1)
        return self

    def get_propety_text_of_element(self, element):
        return element.get_property('textContent')

    def get_text_of_element(self, locator):
        return self.is_visible(locator).text

    def get_text_of_element_by_text_link(self, text_link):
        return self.is_visible_by_link_text(text_link).text

    def get_html_of_element(self, element):
        return element.get_property('outerHTML')

    def wait_time(self, time: int = 1):
        sleep(time)
        return self

    def click_by_linktext(self, linktext: str):
        self.click_element(self.is_visible_by_link_text(linktext))
        self.is_not_visible(self.LOADING_TAG)
        return self

    def open_page_by_url(self, url):
        self.browser.get(url)
        self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
        self.is_not_visible(self.LOADING_TAG)
        return self

    def save_screenshot(self, request):
        test_name = request.node.name
        self.browser.save_screenshot(f'/logs/screen/{self.browser.session_id} + {test_name}.png')

    def back_to_previous_page(self):
        self.browser.back()
        self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
        self.is_not_visible(self.LOADING_TAG)
        return self

    def scroll_page_down(self):
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        return self

    def scroll_page_up(self):
        self.browser.execute_script('window.scrollTo(0, -document.body.scrollHeight);')
        return self

    def scroll_to_element(self, element):
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)


    def delete_text_in_element(self, element):
        element.send_keys(Keys.CONTROL + Keys.BACKSPACE)
        return self

    def click_with_selector(self, locator, verify="visible"):
        """ выполняет клик по элменту с дополнительным указанием верификации элемента
        если верификация выполняется по text или link_text, то вместо локатора подставляется текст элемента
        """
        if verify == "visible":
            self.click_element(self.is_visible(locator))
            return self
        elif verify == "presence":
            self.click_element(self.is_presence(locator))
            return self
        elif verify == "text":
            text = locator
            self.click_element(self.is_visible_by_text(text))
            return self
        elif verify == "link_text":
            link_text = locator
            self.click_element(self.is_visible_by_link_text(link_text))
            return self
        else:
            raise AssertionError("Ошибка, нужно выбрать метод верификации см. подсказку к методу")

    def enter_keys_with_selector(self, input_text, locator, verify="visible"):
        """ выполняет ввод текста в элмент с дополнительным указанием верификации элемента
        если верификация выполняется по text или link_text, то вместо локатора подставляется текст элемента
        """
        if verify == "visible":
            self.clear_and_send_keys(self.is_visible(locator), input_text)
            return self
        elif verify == "presence":
            self.clear_and_send_keys(self.is_presence(locator), input_text)
            return self
        elif verify == "text":
            text = locator
            self.clear_and_send_keys(self.is_visible_by_text(text), input_text)
            return self
        elif verify == "link_text":
            link_text = locator
            self.clear_and_send_keys(self.is_visible_by_link_text(link_text), input_text)
            return self
        else:
            raise AssertionError("Ошибка, нужно выбрать метод верификации см. подсказку к методу")
