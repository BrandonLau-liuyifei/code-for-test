from selenium import webdriver
# from .chrome.webdriver import WebDriver as Chrome  # noqa
import time

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.maximize_window()
# time.sleep(1)
#
# element = driver.find_element_by_id("kw")
# element.send_keys('selenium')
# print(type(element))
# # <class 'selenium.webdriver.remote.webelement.WebElement'>
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.quit()
from selenium.webdriver.common.by import By


class Testcase():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        time.sleep(1)

    def test_id_locate(self):
        element = self.driver.find_element_by_id("kw")
        element.send_keys('selenium')
        print(type(element))
        self.driver.find_element_by_id('su').click()

        time.sleep(3)
        # self.driver.quit()

    def test_name_locate(self):
        # find_element_by_name 方法可能返回多个元素，返回第一个
        # find_element_by_name 方法返回一个集合
        self.driver.find_element_by_name("wd").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

        time.sleep(3)
        self.driver.quit()

    def test_linktext_locate(self):
        self.test_id_locate()
        self.driver.find_element_by_link_text("百度首页").click()

        time.sleep(3)
        self.driver.quit()

    def test_linktext_partial_locate(self):
        self.test_id_locate()
        self.driver.find_element_by_partial_link_text("百度").click()

        time.sleep(3)
        self.driver.quit()

    def test_xpath_locate(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("极客时间")
        self.driver.find_element_by_id("su").click()

        time.sleep(3)
        self.driver.quit()

    def test_tag_locate(self):
        # 一般不能准确地定位
        self.driver.find_element_by_tag_name("input")[0].send_keys("极客时间")
        self.driver.find_element_by_id("su").click()

        time.sleep(3)
        self.driver.quit()

    def test_css_selector_loacate(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("极客时间")
        self.driver.find_element_by_id("su").click()

        time.sleep(3)
        self.driver.quit()

    def test_class_name_locate(self):
        self.driver.find_element_by_class_name("s_ipt").send_keys("极客时间")
        self.driver.find_element_by_id("su").click()

        time.sleep(3)
        self.driver.quit()
    def test_all(self):
        self.driver.find_element(By.ID,value='kw').send_keys("极客时间")
        self.driver.find_element_by_id("su").click()

        time.sleep(3)
        self.driver.quit()



if __name__ == "__main__":
    case=Testcase()
    # case.test_id_locate()
    # case.test_name_locate()
    # case.test_linktext_locate()
    # case.test_linktext_partial_locate()
    # case.test_xpath_locate()
    # case.test_tag_locate()
    # case.test_css_selector_loacate()
    # case.test_class_name_locate()
    case.test_all()