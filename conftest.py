# import pytest
# from selenium import webdriver
#
# @pytest.fixture(params=['chrome'],scope='class')
# def setup_module(request):
#     print('This is setup')
#     if request.param == 'chrome':
#     # global driver
#     #     c_options = webdriver.ChromeOptions()
#     #     c_options.add_argument("--start-maximized")
#         driver = webdriver.Chrome()
#         request.cls.driver=driver
#         driver.get("https://google.com")