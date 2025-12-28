import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators



class OrderPage(BasePage):
    @allure.step("Заполнить имя: {text}")
    def set_first_name_input(self, text):
        self.send_keys_to_element(OrderPageLocators.FIRST_NAME_INPUT, text)

    @allure.step("Заполнить фамилию: {text}")
    def set_last_name_input(self, text):
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_INPUT, text)

    @allure.step("Заполнить адрес: {text}")
    def set_address_input(self, text):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, text)

    @allure.step("Клик по полю выбора станции метро")
    def click_on_metro_station_input(self):
        self.wait_and_click_on_element(OrderPageLocators.METRO_STATION_INPUT)

    @allure.step("Выбрать станцию метро: {station}")
    def click_on_metro_station(self, station):
        self.wait_and_click_on_element(OrderPageLocators.metro_station(station))

    @allure.step("Заполнить номер телефона: {text}")
    def set_phone_number(self, text):
        self.send_keys_to_element(OrderPageLocators.PHONE_NUMBER_INPUT, text)

    @allure.step("Клик по кнопке Далее")
    def click_on_next_button(self):
        self.wait_and_click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Указать дату аренды: {text}")
    def set_date_input(self, text):
        self.send_keys_to_element(OrderPageLocators.RENTAL_DATE_INPUT, text)

    @allure.step("Клик по полю срока аренды")
    def click_on_rental_period_input(self):
        self.wait_and_click_on_element(OrderPageLocators.RENTAL_PERIOD_INPUT)

    @allure.step("Выбрать срок аренды: {text}")
    def click_on_days(self, text):
        self.wait_and_click_on_element(OrderPageLocators.days(text))

    @allure.step("Клик по кнопке Заказать")
    def click_on_order_button(self):
        self.wait_and_click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def click_on_confirm_yes_button(self):
        self.wait_and_click_on_element(OrderPageLocators.CONFIRM_YES_BUTTON)
    
    @allure.step("Получить заголовок подтверждения заказа")
    def get_order_confirmation_title(self):
        title = self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRMATION_TITLE)
        full_text = title.text
        first_line = full_text.split('\n')[0].strip()
        return first_line
    
    @allure.step("Клик по кнопке Проверить статус")
    def click_on_check_status_button(self):
        self.wait_and_click_on_element(OrderPageLocators.CHECK_STATUS_BUTTON)   
