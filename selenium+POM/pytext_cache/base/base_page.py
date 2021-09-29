# 开发人员:Sun
# 开发时间:2021/6/26  23:48:45
# 文件名称:base_page.PY
# 开发工具:PyCharm


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

