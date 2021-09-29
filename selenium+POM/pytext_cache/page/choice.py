# 开发人员:Sun
# 开发时间:2021/6/28  19:53:04
# 文件名称:choice.PY
# 开发工具:PyCharm
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
class Tools:
    def __init__(self,driver):
        self.driver = driver
    #访问
    def open(self,url):
        self.driver.get(url)
    # 元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)
    # 输入 定位 
    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)
    #点击
    def on_click(self,loc):
        self.locator(loc).click()
    #等待
    def wait(self):
        time.sleep(3)
    #关闭
    def quit(self):
        self.driver.quit()
#继承父类（Tools）
class ChoicePage(Tools):
    # 页面地址
    url = 'http://39.98.138.157/shopxo/'
    # 页面元素
    search_input = (By.NAME,'wd')
    search_btn = (By.ID,'ai-topsearch')
    # 流程
    def search(self,txt):
        self.input(self.search_input,txt)
        self.on_click(self.search_btn)

if __name__ == '__main__':
    dr = ChoicePage(webdriver.Chrome(r'C:\Users\Sun\Desktop\selenium+POM\chromedriver.exe'))
    dr.search('手机')