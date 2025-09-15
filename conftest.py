import pytest

from selenium import webdriver
import time

@pytest.fixture(params=['chrome'],scope='class')
def setup_teardown(request):
    if request.param == 'chrome':
        c_options = webdriver.ChromeOptions()
        c_options.add_argument("headless")
        driver = webdriver.Chrome(options=c_options)
        request.cls.driver=driver
        driver.get("https://google.com")
        yield
        driver.quit()

