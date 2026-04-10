import allure
import pytest
from pages.main_page import MainPage
from data.data_questions import faq_data


@allure.story('Блок "Вопросы о важном"')
class TestQuestions:

    @allure.title('Проверка ответов на вопросы из блока "Вопросы о важном"')
    @allure.description('Проверяем, что текст ответа на каждый вопрос соответствует ожидаемому')
    @pytest.mark.parametrize('faq_item', faq_data)
    def test_question_answer(self, open_main_page, faq_item):
        
        main_page = MainPage(open_main_page)
        
        answer_text = main_page.get_faq_answer(
            faq_item["question_locator"],
            faq_item["answer_locator"]
        )
        assert faq_item["expected_text"] in answer_text