from selenium import webdriver
import time,os

class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/framesTest.htm")

    def test_frame(self):
        top = self.driver.find_element_by_name("top")
        self.driver.switch_to.frame(top)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/a[1]").click()
        time.sleep(5)

        self.driver.switch_to.default_content()

        second = self.driver.find_element_by_xpath("/html/frameset/frame[2]")
        self.driver.switch_to.frame(second)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/a[1]").click()
        time.sleep(5)

        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test_frame()

"""
frame标签有3种：
frameset 与其他普通标签没有区别，不会影响正常的定位
frame 通iframe，通过以下方法进行定位：
1. switch_to.frame(reference)  切换frame，reference为必要参数，用来定位frame，可以传入id、name、index以及slenium的WebElement对象
2. switch_to.default_content()  返回主文档
3. switch_to.parent_frame()  返回父文档
"""