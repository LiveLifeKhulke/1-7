import pytest

from selenium import webdriver
import time

@pytest.fixture(params=['chrome'],scope='class')
def setup_module(request):
    print('This is setup')
    if request.param == 'chrome':
    # global driver
        c_options = webdriver.ChromeOptions()
        c_options.add_argument("--headless")
        driver = webdriver.Chrome(options=c_options)
        request.cls.driver=driver
        driver.get("https://google.com")
        time.sleep(5)