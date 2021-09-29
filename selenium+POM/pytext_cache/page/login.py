#登录页面
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
#封装成为一个工具箱
class Tools:
    # 浏览器
    # driver = webdriver.Chrome()
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
class LoginPage(Tools):
    url='http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    #页面元素
    username = (By.NAME,'accounts')
    password = (By.NAME,'pwd')
    loginbtn = (By.XPATH,"/html[@class='js cssanimations']/body/div[@class='am-g my-content']/div[@class='am-container user-login-container']/div[@class='am-u-sm-12 am-u-md-6 am-u-lg-4 container-right']/div[@class='user-form-container']/form[@class='am-form form-validation']/div[@class='am-form-group am-form-group-refreshing']/button[@class='am-btn am-btn-primary am-radius am-btn-sm btn-loading-example']")
    def login(self,usr,pwd):
        self.open(self.url)
        self.input(self.username,usr)
        self.input(self.password,pwd)
        self.on_click(self.loginbtn)
#测试
if __name__ == '__main__':
    driver=LoginPage(webdriver.Chrome(r'C:\Users\Sun\Desktop\selenium+POM\chromedriver.exe'))
    driver.login('sun','123456')
