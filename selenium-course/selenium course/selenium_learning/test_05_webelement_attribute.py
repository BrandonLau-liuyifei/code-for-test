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