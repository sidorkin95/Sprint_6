import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data.data_order import data_order_set_1, data_order_set_2

@allure.story('Заказ самоката')
class TestOrderScooter:

    @allure.title('Позитивный сценарий заказа самоката через верхнюю кнопку')
    @allure.description('Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу')
    def test_positive_order_flow_with_top_button(self, open_main_page):

        driver = open_main_page
        main_page = MainPage(driver)
        main_page.click_on_order_button_top()
        
        order_page = OrderPage(driver)

        order_page.fill_customer_order(
            name=data_order_set_1["name"],
            surname=data_order_set_1["surname"],
            address=data_order_set_1["address"],
            index=data_order_set_1["index"],
            number=data_order_set_1["number"]
        )


        order_page.fill_rental_form(
            date=data_order_set_1["date"],
            period=data_order_set_1["rental_period"],
            color=data_order_set_1["color"],
            comment=data_order_set_1["comment"]
        )
        
        order_page.click_order_button()
        order_page.click_confirm_yes_button()
        
        assert order_page.is_order_successful(), "Заказ не создан"

    @allure.title('Позитивный сценарий заказа самоката через кнопку снизу')
    @allure.description('Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу')
    def test_positive_order_flow_with_low_button(self, open_main_page):

        driver = open_main_page
        main_page = MainPage(driver)

        main_page.click_on_order_button_low()

        order_page = OrderPage(driver)

        order_page.fill_customer_order(
            name=data_order_set_2["name"],
            surname=data_order_set_2["surname"],
            address=data_order_set_2["address"],
            index=data_order_set_2["index"],
            number=data_order_set_2["number"]
        )

        order_page.fill_rental_form(
            date=data_order_set_2["date"],
            period=data_order_set_2["rental_period"],
            color=data_order_set_2["color"],
            comment=data_order_set_2["comment"]
        )
        
        order_page.click_order_button()
        order_page.click_confirm_yes_button()
        
        assert order_page.is_order_successful(), "Заказ не создан"