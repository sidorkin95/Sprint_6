import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Найти все элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step("Заполнить поле")
    def send_keys(self, locator, text):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element.text
    
    @allure.step("Ожидать видимость элемента")
    def wait_for_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Ожидать кликабельность элемента")
    def wait_for_clickable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))
    
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
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url