from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    RENTAL_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_INPUT = (By.XPATH, "//span[@class='Dropdown-arrow']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle')]")
    CONFIRMATION_MODAL_FORM = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_CONFIRMATION_TITLE = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")

    @staticmethod
    def metro_station(text):
        return (By.XPATH, f"//div[contains(text(), '{text}')]")

    @staticmethod
    def days(text):
        return (By.XPATH, f"//div[@class='Dropdown-option' and contains(text(), '{text}')]")