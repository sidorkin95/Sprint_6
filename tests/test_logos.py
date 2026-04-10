import allure
from pages.main_page import MainPage
from urls import Urls


@allure.story('Навигация через логотипы')
class TestLogos:


    @allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    @allure.title('Логотип "Самоката" ведёт на главную страницу')
    def test_scooter_logo_redirects_to_main(self, open_main_page):

        driver = open_main_page

        main_page = MainPage(driver)


        main_page.click_on_order_button_top()

        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        assert current_url == Urls.BASE_URL



    @allure.title('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    @allure.title('Логотип "Самоката" ведёт на главную страницу')
    def test_yandex_logo_opens_dzen(self, open_main_page):

        driver = open_main_page
        main_page = MainPage(driver)

        main_page.click_yandex_logo()

        main_page.switch_to_new_window()
        main_page.wait_for_url_loaded()
        
        current_url = main_page.get_current_url()
        assert 'dzen.ru' in current_url 
        