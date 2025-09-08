import pytest

@pytest.mark.usefixtures('setup_module')
@pytest.mark.smoke1
@pytest.mark.parametrize('title,url',[('Google','google')])
class Test_demo:
    def test_demo(self,title,url):
        print('Hi , this is test')
        assert title in self.driver.title
        assert url in self.driver.current_url
        