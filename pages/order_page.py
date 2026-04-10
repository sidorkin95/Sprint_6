import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

class OrderPage(MainPageLocators, OrderPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @allure.step('Кликнуть по кнопке "Заказать" вверху')
    def click_on_order_button_top(self):
    
        self.driver.find_element(*self.order_button_top).click()    
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.first_name))
        
    
    @allure.step('Прокрутить страницудо кнопки "Заказать" внизу')
    def scroll_to_questions(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_button_low))
        
        element = self.driver.find_element(*self.order_button_low)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
    @allure.step('Кликнуть по кнопке "Заказать" внизу')
    def click_on_order_button_low(self):
    
        self.driver.find_element(*self.order_button_low).click()
         
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.first_name))
    
    @allure.step('Заполнить поле "Имя" значением: {name}')
    def fill_first_name_field(self, name):
        self.driver.find_element(*self.first_name).send_keys(name)

    @allure.step('Заполнить поле "Фамилия" значением: {surname}')
    def fill_last_name_field(self, surname):
        self.driver.find_element(*self.last_name).send_keys(surname)

    @allure.step('Заполнить поле "Адрес" значением: {address}')
    def fill_address_to_deliver_order_field(self, address):
        self.driver.find_element(*self.address_to_deliver_order).send_keys(address)

    @allure.step("Выбираем станцию метро")
    def set_metro(self, index): 
        self.driver.find_element(*self.metro_input).click()

        self.wait.until(expected_conditions.visibility_of_element_located(self.metro_options))

        stations = self.driver.find_elements(*self.metro_options) 
        stations[index].click()


    @allure.step('Заполнить поле "Телефон" значением: {number}')
    def fill_telephone_field(self, number):
        self.driver.find_element(*self.telephone).send_keys(number)

    @allure.step('Кликнуть по кнопке "Далее"')
    def click_on_button_next(self):
        self.driver.find_element(*self.button_next).click()

    @allure.step('Открывается форма "Про аренду"')
    def get_header_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.header_page))
    
    @allure.step('Заполнить поле "Когда привезти самокат" значением: {date}')
    def fill_date_field(self, date):
        self.driver.find_element(*self.date_field).send_keys(date)

    def click_rental_header(self):
        self.driver.find_element(*self.rental_header).click()

    @allure.step('Выбрать срок аренды')
    def set_rental_period(self, period):
        self.driver.find_element(*self.rental_dropdown).click()

        self.driver.find_element(*self.rental_periods[period]).click()


    @allure.step("Выбрать цвет")
    def set_color(self, color):
        if color.lower() == "black":
            self.driver.find_element(*self.color_black).click()
        elif color.lower() == "grey":
            self.driver.find_element(*self.color_grey).click()

    @allure.step("Оставить комментарий курьеру")
    def fill_comment_for_courier_field(self, comment):
        self.driver.find_element(*self.comment_for_courier).send_keys(comment)

    @allure.step('На форме "Про аренду" кликнуть по кнопке "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Открывается форма "Хотите оформить заказ?"')
    def get_modal_header(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.modal_header))
        
    @allure.step('На форме "Хотите оформить заказ?" кликнуть по кнопке "Да"')
    def click_confirm_yes_button(self):

        
        confirm_button = self.wait.until(
            expected_conditions.element_to_be_clickable(self.confirm_yes_button))
        confirm_button.click()
        
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.success_modal))

    @allure.step("Ожидаем появления окна с подтверждением заказа")
    def wait_for_success_modal(self):

        return self.wait.until(
            expected_conditions.visibility_of_element_located(self.success_modal))
    
    
    @allure.step("Получаем текст из окна подтверждения заказа")
    def get_success_text(self) -> str:
        modal = self.wait.until(
            expected_conditions.visibility_of_element_located(self.success_modal))
        return modal.text

    def complete_order(self, name, surname, address, number,index, date, period, color, comment):
        self.fill_first_name_field(name)
        self.fill_last_name_field(surname)
        self.fill_address_to_deliver_order_field(address)
        self.fill_telephone_field(number)
        self.set_metro(index)
        self.click_on_button_next()

        self.fill_date_field(date)
        self.click_rental_header()
        self.set_rental_period(period)
        self.set_color(color)
        self.fill_comment_for_courier_field(comment)

        self.click_order_button()
        self.click_confirm_yes_button()
