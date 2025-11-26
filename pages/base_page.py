from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    def wait_and_scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_and_click_on_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    def send_keys_to_element(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)
    
    def switch_to_new_window(self):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
            
    def get_current_url(self, url):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.url_contains(url))
        return self.driver.current_url