from selenium import webdriver
import time,os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test_01(self):
        self.driver.execute_script("alert('test')")
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    def test_02(self):
        js = "return document.title"
        title = self.driver.execute_script(js)
        print(title)

    def test_03(self):
        js = "var q = document.getElementById('kw'); q.style.border='2px solid red'"
        self.driver.execute_script(js)

    def test_04(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

if __name__ == '__main__':
    case = TestCase()
    # case.test_01()
    # case.test_02()
    # case.test_03()
    case.test_04()

"""
selenium执行javascript脚本：
excute_script 同步执行
excute_async_script 异步执行
通过执行javascript实现页面滚动
"""
