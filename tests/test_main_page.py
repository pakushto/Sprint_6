import pytest
import allure
from pages.main_page import MainPage
from data import MainPageTestData


class TestMainPage:

    @pytest.mark.parametrize('index', range(8))
    @allure.title("FAQ открывается по клику на вопрос")
    def test_faq_answer_opens_on_click(self, driver, index):
        main_page = MainPage(driver)
        main_page.scroll_to_faq()
        main_page.click_on_faq_question_by_index(index)
        current_question_text = main_page.get_faq_question_text_by_index(index)
        current_answer_text = main_page.get_faq_answer_text_by_index(index)
        
        assert current_question_text == MainPageTestData.FAQ_QUESTIONS[index]
        assert current_answer_text == MainPageTestData.FAQ_ANSWERS[index]