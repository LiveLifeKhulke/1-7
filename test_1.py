import pytest

@pytest.mark.usefixtures('setup_module')
@pytest.mark.smoke1
@pytest.mark.parametrize('title,url',[('Google','google')])
class Test_demo:
    def test_demo(self,title,url):
        print('Hi , this is test')
        if 3>5:
            assert title in self.driver.title
            assert url in self.driver.current_url
        else:
            pass

# import requests
#
# @pytest.mark.smoke1
# def test_demo():
#     url = 'https://fake-json-api.mock.beeceptor.com/user'
#     response = requests.get(url)
#     json_response=response.json()
#     assert not response.status_code == 201
#     print(json_response['paths'][2])