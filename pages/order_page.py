import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    
    @allure.step('Заполнить поле "Имя" значением: {name}')
    def fill_first_name_field(self, name):
        self.send_keys(OrderPageLocators.first_name, name)

    @allure.step('Заполнить поле "Фамилия" значением: {surname}')
    def fill_last_name_field(self, surname):
        self.send_keys(OrderPageLocators.last_name, surname)

    @allure.step('Заполнить поле "Адрес" значением: {address}')
    def fill_address_to_deliver_order_field(self, address):
        self.send_keys(OrderPageLocators.address_to_deliver_order, address)

    @allure.step("Выбираем станцию метро")
    def set_metro(self, index): 
        self.click(OrderPageLocators.metro_input)
        stations = self.find_elements(OrderPageLocators.metro_options) 
        stations[index].click()

    @allure.step('Заполнить поле "Телефон" значением: {number}')
    def fill_telephone_field(self, number):
        self.send_keys(OrderPageLocators.telephone, number)

    @allure.step('Кликнуть по кнопке "Далее"')
    def click_on_button_next(self):
        self.click(OrderPageLocators.button_next)

    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_customer_order(self, name, surname, address, index, number):
        self.fill_first_name_field(name)
        self.fill_last_name_field(surname)
        self.fill_address_to_deliver_order_field(address)
        self.set_metro(index)
        self.fill_telephone_field(number)
        self.click_on_button_next()

    
    @allure.step('Заполнить поле "Когда привезти самокат" значением: {date}')
    def fill_date_field(self, date):
        self.send_keys(OrderPageLocators.date_field, date)

    def click_rental_header(self):
        self.click(OrderPageLocators.rental_header)

    @allure.step('Выбрать срок аренды')
    def set_rental_period(self, period):
        self.click(OrderPageLocators.rental_dropdown)
        self.click(OrderPageLocators.rental_periods[period])

    @allure.step("Выбрать цвет")
    def set_color(self, color):
        if color.lower() == "black":
            self.click(OrderPageLocators.color_black)
        elif color.lower() == "grey":
            self.click(OrderPageLocators.color_grey)

    @allure.step("Оставить комментарий курьеру")
    def fill_comment_for_courier_field(self, comment):
        self.send_keys(OrderPageLocators.comment_for_courier, comment)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rental_form(self, date, period, color, comment):
        self.fill_date_field(date)
        self.click_rental_header()
        self.set_rental_period(period)
        self.set_color(color)
        self.fill_comment_for_courier_field(comment)
        

    @allure.step('На форме "Про аренду" кликнуть по кнопке "Заказать"')
    def click_order_button(self):
        self.click(OrderPageLocators.order_button)

    @allure.step('На форме "Хотите оформить заказ?" кликнуть по кнопке "Да"')
    def click_confirm_yes_button(self):
        self.click(OrderPageLocators.confirm_yes_button)
    
    @allure.step("Проверить, что заказ успешно создан")
    def is_order_successful(self):
        self.wait_for_visible(OrderPageLocators.success_modal)
        title = self.get_text(OrderPageLocators.success_title)
        return "Заказ оформлен" in title
