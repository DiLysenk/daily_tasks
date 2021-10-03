
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException # в начале файла

import math


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


class ProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self, wd):
        return wd.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019')

    param = 'promo=newYear'

    def find_basket(self, wd):
        return wd.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket').click()




