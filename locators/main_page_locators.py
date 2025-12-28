from selenium.webdriver.common.by import By


class MainPageLocators:
    @staticmethod
    def faq_question(index):
        return (By.XPATH, f"//div[@id='accordion__heading-{index}']")
    
    @staticmethod
    def faq_answer(index):
        return (By.XPATH, f"//div[@id='accordion__panel-{index}']")
    
    @staticmethod
    def order_button_locator(position):
        mapping = {
            "top": MainPageLocators.ORDER_BUTTON_TOP,
            "bottom": MainPageLocators.ORDER_BUTTON_BOTTOM,
        }
        return mapping[position]
    
    FAQ_BLOCK = (By.XPATH, "//div[@class='accordion']")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home')]/button[text()='Заказать']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")