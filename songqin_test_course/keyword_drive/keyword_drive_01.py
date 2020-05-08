# 关键字驱动是：RobotFrameWork，基于表格编程来实现的关键字驱动测试框架，通过一个特定的关键词，调用指定的对应事务操作
# 将操作步骤进行封装
from selenium import webdriver

class KeywordDemo(object):
    # 初始化
    def __init__(self, browser_type,url):
        self.browser_init(browser_type)
        self.visit(url)

    # 隐形等待
    def implicitly_wait(self,seconds):
        self.driver.implicitly_wait(seconds)

    # 创建webdriver对象
    def browser_init(self, browser_type):
        if browser_type == "chrome":
            self.driver = webdriver.Chrome()
            return self.driver
        elif browser_type == "firefox":
            driver = webdriver.Firefox()
            return self.driver
        else:
            driver = webdriver.Ie()
            return self.driver

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 定位元素
    def locator(self,el_type,value):
        if el_type == "id":
            el = self.driver.find_element_by_id(value)
        elif el_type == "name":
            el = self.driver.find_element_by_class_name(value)
        elif el_type == "xpath":
            el = self.driver.find_element_by_xpath(value)
        return el
    """# 定位元素
    def locator(self,value):
        return self.driver.find_element(*value)"""

    # 输入
    def input_text(self,el_type,value,value1):
        self.locator(el_type,value).send_keys(value1)

    # 点击
    def click(self,el_type,value):
        self.locator(el_type,value).click()

if __name__=='__main__':
    kd = KeywordDemo('chrome','http://www.baidu.com')
    kd.implicitly_wait(10)
    kd.input_text("id","kw","虚竹")
    kd.click("id","su")
    kd.click("xpath",'//*[@id="1"]/h3/a')


