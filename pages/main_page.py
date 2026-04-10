import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик на вопрос и получение ответа")
    def get_faq_answer(self, question_locator, answer_locator):
        self.scroll_to_element(question_locator)
        self.click(question_locator)
        return self.get_text(answer_locator)

    @allure.step('Кликнуть по кнопке "Заказать" вверху')
    def click_on_order_button_top(self):
        self.click(MainPageLocators.order_button_top)

    @allure.step('Кликнуть по кнопке "Заказать" внизу')
    def click_on_order_button_low(self):
        self.scroll_to_element(MainPageLocators.order_button_low)
        self.click(MainPageLocators.order_button_low)
        
    @allure.step('Клик по логотипу самоката')
    def click_scooter_logo(self):
        self.click(MainPageLocators.scooter_logo)

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(MainPageLocators.yandex_logo)
