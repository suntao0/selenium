# 开发人员:Sun
# 开发时间:2021/7/12  21:53:56
# 文件名称:run.PY
# 开发工具:PyCharm
#执行用例
import pytest
import os
if __name__ == '__main__':
    # 执行用例生成测试报告  测试数据   文件夹
    pytest.main(['-s','./test_case/test_case.py','--alluredir','./allure-results'])
    # 生成测试报告  测试数据
    os.system('allure generate ./allure-results -o ./allure-reports')