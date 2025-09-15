import pytest

@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.parametrize('title',[('google'),('gooGle')])
class Test_demo:
    def test_demo(self,title):
        assert self.driver.title in title
