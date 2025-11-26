import pytest
from selenium import webdriver

from data import Urls

@pytest.fixture(scope='function')
def driver(request):
    browser = webdriver.Firefox()

    browser.get(Urls.SCOOTER_URL)

    yield browser

    browser.quit()