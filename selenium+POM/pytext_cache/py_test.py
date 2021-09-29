# 开发人员:Sun
# 开发时间:2021/6/28  21:30:33
# 文件名称:py_test.PY
# 开发工具:PyCharm
import pytest
class cestCase:
    #测试程   测试   登录---选商品----下单   打开浏览器
    def setup_class(self):
        print('类的前置条件，打开浏览器')
    def teardown_class(self):
        print('类的后置条件')
    def setup(self):
        print('用例执行前做事情，打开浏览器')
    def teardown(self):
        print('用例执行后做事情')

    # @pytest.mark.run(order=2)
    # 一条用例代表一个test方法
    def test_01(self):
        print('第一条用例')
        assert 1 == '1',  '1等于 字符串‘1’'
    # @pytest.mark.run(order=1)
    def test_02(self):
        print('第二条用例')
        assert 1 == 1, '1等于 1'

    # @pytest.mark.ss
    # @pytest.mark.run(order=3)
    def test_03(self):
        print('第三条用例')
        assert 1 == 2, '1等于2'

# 执行1.main  pytest.main  
# 2.终端中执行  指定运行哪个文件  结果显示出来
if __name__ == '__main__':
    pytest.main(['-s','-v','py_test.py'])
