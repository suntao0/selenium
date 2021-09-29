# 开发人员:Sun
# 开发时间:2021/6/28  20:16:26
# 文件名称:text_case.PY
# 开发工具:PyCharm
import pytest
import time
from selenium import webdriver
from page.choice import ChoicePage
from page.login import LoginPage
from pytext_cache.config.yamlload import loadyaml

class TestCase:
    # 持有cls参数，可以来调用类的属性，类的方法，实例化对象等
    def setup_class(cls) -> None:
        cls.driver = webdriver.Chrome(r'C:\Users\Sun\Desktop\selenium+POM\chromedriver.exe')
        cls.lp = LoginPage(cls.driver)
        cls.cp = ChoicePage(cls.driver)

    def teardown_class(cls) -> None:
        cls.driver.quit()
    @pytest.mark.parametrize('utxt', loadyaml('../data/login.yaml'))
    def test_01(self, utxt):
        self.lp.login(utxt['uname'], utxt['pwd'])
        time.sleep(3)
    def test_02(self):
        self.cp.search('手机')
        time.sleep(3)
if __name__ == '__main__':
    pytest.main()
