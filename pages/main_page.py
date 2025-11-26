import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Urls


class MainPage(BasePage):
    @allure.step("Прокрутить до FAQ")
    def scroll_to_faq(self):
        self.wait_and_scroll_to_element(MainPageLocators.FAQ_BLOCK)

    @allure.step("Прокрутить до кнопки 'Заказать'")
    def scroll_to_order_button(self, position):
        self.wait_and_scroll_to_element(MainPageLocators.order_button_locator(position))    

    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_on_faq_question_by_index(self, index):
        self.wait_and_click_on_element(MainPageLocators.faq_question(index))

    @allure.step("Получить текст вопроса FAQ с индексом {index}")
    def get_faq_question_text_by_index(self, index):
        question = self.wait_and_find_element(MainPageLocators.faq_question(index))
        return question.text
    
    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_faq_answer_text_by_index(self, index):
        answer = self.wait_and_find_element(MainPageLocators.faq_answer(index))
        return answer.text
    
    @allure.step("Клик по кнопке Заказать на главной")
    def click_on_order_button(self, position):
        self.wait_and_click_on_element(MainPageLocators.order_button_locator(position))

    @allure.step("Клик по логотипу Самоката")
    def click_on_scooter_logo(self):
        self.wait_and_click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекс")
    def click_on_yandex_logo(self):
        self.wait_and_click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Получить URL главной страницы")
    def get_main_page_url(self):
        return self.get_current_url(Urls.SCOOTER_URL)
        
    @allure.step("Получить URL Дзена")
    def get_dzen_url(self):
        return self.get_current_url(Urls.DZEN_URL)
