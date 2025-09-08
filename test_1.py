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

@pytest.mark.usefixtures('setup_module')
@pytest.mark.smoke1
@pytest.mark.parametrize('title,url',[('Google','google'),('GOgle','Google')])
class Test_demo:
    def test_demo(self,title,url):
        print('Hi , this is test')
        assert title in self.driver.title
        assert url in self.driver.current_url

# import requests
#
# @pytest.mark.smoke1
# def test_demo():
#     url = 'https://fake-json-api.mock.beeceptor.com/user'
#     response = requests.get(url)
#     json_response=response.json()
#     assert not response.status_code == 201
#     print(json_response['paths'][2])