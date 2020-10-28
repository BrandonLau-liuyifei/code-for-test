from selenium import webdriver
import time,os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://sahitest.com/demo/clicks.htm")
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_mouse(self):
        # 双击
        btn_01 = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        ActionChains(self.driver).double_click(btn_01).perform()
        time.sleep(2)
        # 单击
        btn_02 = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        ActionChains(self.driver).click(btn_02).perform()
        time.sleep(2)
        # 右键
        right_02 = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        ActionChains(self.driver).context_click(right_02).perform()
        time.sleep(2)

    def tsst_keyword(self):
        kw = self.driver.find_element_by_id("kw")
        kw.send_keys("萧敬腾")
        kw.send_keys(Keys.CONTROL,"a")
        time.sleep(5)
        kw.send_keys(Keys.CONTROL,"x")
        time.sleep(5)
        kw.send_keys(Keys.CONTROL,"v")
        time.sleep(5)

        el = self.driver.find_element_by_link_text("百度首页")
        ActionChains(self.driver).move_to_element(el).click().perform()
        time.sleep(2)
if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    case.tsst_keyword()

"""
鼠标操作：
click(on_element=None)
click_and_hold(on_element=None)
context_click()


"""

