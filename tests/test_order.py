import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage

@allure.story('Заказ самоката')    
@allure.title('Позитивный сценарий заказа самоката через верхнюю кнопку')
@allure.description('Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу')
def test_positive_order_flow_with_top_button(driver):

    main_page = MainPage(driver)
    main_page.open_main_page()

    order_page = OrderPage(driver)

    order_page.click_on_order_button_top()
    
    order_page.complete_order(
        name="Валерий",
        surname="Барчук",
        address="Москва, ул. Примерная, д. 1", 
        index= 6,
        number="79543212211",
        date="11.04.2026",
        period="сутки",
        color="black",
        comment=""
    )
    
    
    success_modal = order_page.wait_for_success_modal()
    assert success_modal.is_displayed()

    success_text = order_page.get_success_text()
    assert "Заказ оформлен" in success_text

@allure.story('Заказ самоката')
@allure.title('Позитивный сценарий заказа самоката через кнопку снизу')
@allure.description('Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу')
def test_positive_order_flow_with_low_button(driver):

    main_page = MainPage(driver)
    main_page.open_main_page()


    order_page = OrderPage(driver)

    order_page.scroll_to_questions()

    order_page.click_on_order_button_low()
    
    order_page.complete_order(
        name="Петр",
        surname="Соловьев",
        address="г.Москва, ул. Ударная, д. 1", 
        index= 3,
        number="79635659021",
        date="17.04.2026",
        period="двое суток",
        color="gray",
        comment="Домофон не работает"
    )
    
    
    success_modal = order_page.wait_for_success_modal()
    assert success_modal.is_displayed()

    success_text = order_page.get_success_text()
    assert "Заказ оформлен" in success_text