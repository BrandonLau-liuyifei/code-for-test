from selenium import webdriver
import time, os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + "/test_11_wait.html"
        self.driver.get(file_path)

    def test_wait(self):
        self.driver.find_element_by_id("btn").click()
        # 显示等待
        wait = WebDriverWait(self.driver,1)
        wait.until(ec.text_to_be_present_in_element((By.ID,"id2"),"id 2"))
        print(self.driver.find_element_by_id("id2").text)
        print("ok")

if __name__ == '__main__':
    case=TestCase()
    case.test_wait()


"""
等待条件：
title_is 判断title是否出现  布尔值
title_contains 判断title，是否包含某些字符 布尔值
presence_of_element_located 判断元素是否在DOM树中，并代表元素一定可见  element
visiblity_of_element_located  判断元素是否在DOM树中，并宽度和高度都大于0 element
visible_of 判断元素是否可见，如果可见则返回这个元素 element
presence_of_all_elements_located 判断至少一个元素在DOM树中 list
visible_of_any_elements_located 判断至少一个元素在页面中可见 list
text_to_be_present in _element 判断指定的元素中是否包含了预期的字符串 布尔值
text_to_be_present_in_element_value 判断指定元素的属性值是否包含了预期的字符串 布尔值
frame_to_be_available_and_switch_to_it 判断frame是否可以switch进去 布尔值
invisibility_of_element_located 判断某个元素是否存在于DOM中或不可见 布尔值
element_to_be_clickable 判断某个元素是否可见并且是enable的，代表可点击 布尔值
staleness_of 等待某个元素从DOM树中移除 布尔值
element_to_be_selected 判断某个元素是否选中了，一般用在下拉框 布尔值
element_selection_state_to_be 判断某个元素的选中状态是否符合预期 布尔值
element_located_selection_state_to_be 判断某个元素的选中状态是否符合预期 布尔值
alert_is_present 判断页面上是否存在告警 alert
"""
