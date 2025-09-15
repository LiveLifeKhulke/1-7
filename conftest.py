import pytest

from selenium import webdriver
import time

@pytest.fixture(params=['chrome'],scope='class')
def setup_teardown(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        request.cls.driver=driver
        driver.get("https://google.com")
        yield
        driver.quit()

