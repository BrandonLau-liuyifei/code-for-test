from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement


class TestCase():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/linkTest.htm")

    def test_webelement_proc(self):
        e = self.driver.find_element_by_id("t1")
        e1 = WebElement
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)

    def test_webelement_method(self):
        e = self.driver.find_element_by_id("t1")
        e.send_keys("liuyifei")
        time.sleep(2)

        print(e.get_attribute("type"))
        print(e.get_attribute("name"))
        print(e.get_attribute("value"))
        print(e.value_of_css_property("font"))
        print(e.value_of_css_property("color"))
        print(e.value)

        time.sleep(2)
        e.clear()

    def test_method2(self):
        form_element = self.driver.find_element_by_xpath("/html/body/form[1]")
        form_element.find_element_by_id("t1").send_keys("hahaha")

if __name__ == "__main__":
    case = TestCase()
    # case.test_webelement_proc()
    # case.test_webelement_method()
    case.test_method2()



"""
webElement相关属性
    id 标示
    size 大小
    rect 宽高和人坐标
    tag_name 标签名称
    text 文本内容
webElement相关方法
    send_keys() 输入内容
    clear()     清空内容
    click()     单击
    get_attribute() 获取属性值
    is_selected()   是否被选中
    is_enabled()    是否可用
    is_displayed()  是否显示
    value_of_css_property() css属性值
"""