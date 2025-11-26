import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import OrderPageTestData, Urls

class TestOrderPage:

    @allure.title("Оформление заказа самоката")
    @pytest.mark.parametrize('case', OrderPageTestData.TEST_CASES)
    def test_order_scooter(self, driver, case):
        main_page = MainPage(driver)
        main_page.scroll_to_order_button(case["position"])
        main_page.click_on_order_button(case["position"])
        
        order_page = OrderPage(driver)
        order_page.set_first_name_input(case["first_name"])
        order_page.set_last_name_input(case["last_name"])
        order_page.set_address_input(case["address"])
        order_page.click_on_metro_station_input()
        order_page.click_on_metro_station(case["metro_station"])
        order_page.set_phone_number(case["phone_number"])
        order_page.click_on_next_button()
        order_page.set_date_input(case["date"])
        order_page.click_on_rental_period_input()
        order_page.click_on_days(case["days"])
        order_page.click_on_order_button()
        order_page.click_on_confirm_yes_button()
        order_confirmation_title = order_page.get_order_confirmation_title()
        order_page.click_on_check_status_button()
        main_page.click_on_scooter_logo()
        current_page_url = main_page.get_main_page_url()
        main_page.click_on_yandex_logo()
        main_page.switch_to_new_window()
        dzen_url = main_page.get_dzen_url()
        
        assert order_confirmation_title == OrderPageTestData.CONFIRM_TITLE
        assert current_page_url == Urls.SCOOTER_URL
        assert Urls.DZEN_URL in dzen_url 