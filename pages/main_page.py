import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators

class MainPage(MainPageLocators):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.question_1))

    @allure.step('Прокрутить страницу до блока с вопросами')
    def scroll_to_questions(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.question_8))
        element = self.driver.find_element(*self.question_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажать на вопрос: {question_locator}')
    def click_on_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    @allure.step('Получить текст ответа для: {answer_locator}')
    def get_answer_text(self, answer_locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(answer_locator))
        return self.driver.find_element(*answer_locator).text
    
    @allure.step('Клик по логотипу самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def has_new_window(self, driver):

        return len(driver.window_handles) > 1

    @allure.step("Переключиться на новое окно браузера")
    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(self.has_new_window)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return original_window
    
    def wait_for_url_loaded(self): 
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains('dzen.ru'))
        
    
    # Возвращает текущий URL страницы
    def get_current_url(self):
        return self.driver.current_url