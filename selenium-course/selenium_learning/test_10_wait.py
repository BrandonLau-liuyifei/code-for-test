from selenium import webdriver
import time,os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_sleep(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(3)  #阻塞线程 blocking wait
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.driver.quit()

    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # time.sleep(3)  # 阻塞线程
        self.driver.find_element_by_id("su").click()
        # time.sleep(3)
        self.driver.quit()

    def test_webdriverwait(self):
        wait = WebDriverWait(self.driver,2)
        wait.until(ec.title_is("百度一下，你就知道"))
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # time.sleep(3)  # 阻塞线程
        self.driver.find_element_by_id("su").click()
        # time.sleep(3)
        self.driver.quit()



if __name__ == "__main__":
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_webdriverwait()
"""
selenium的三种等待方式
ui测试自动化中，
环境不稳定或网络慢，页面不做处理的话，代码会由于找不到找元素会报错。
页面如果使用ajax异步加载机制。
常见3中等待方式
time.sleep() 效率慢，一般不用

implicitly_wait() 隐式等待，对整个driver周期使用，设置一次即可。

webdriverwair() 显示等待
webdriverwait参数:
driver-传入webdriver实例
timeout-超时时间，等待的最长时间
poll_frequency-调用until或not_until中的方法的间隔时间，默认0.5s
ignored_exceptions-忽略的异常

两种方法，until与until_not
method-在等待期间，每个一段时间调用这个传入的方法，直到返回值不是false
message-如果超时，抛出TimeoutException,将message传入异常
"""
