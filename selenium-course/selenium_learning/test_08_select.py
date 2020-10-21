from selenium import webdriver
import time
import os

from selenium.webdriver.support.select import Select


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        path =os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///"+path+"/test_08_select.html"
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element_by_id("provise")
        select = Select(se)
        # select.select_by_index(2)
        # time.sleep(2)
        # select.select_by_value("bj")
        # time.sleep(2)
        # select.select_by_visible_text("天津")
        # time.sleep(2)
        # 下拉框多选的情况情况
        # for i in range(3):
        #     select.select_by_index(i)
        #     time.sleep(3)
        # time.sleep(3)
        # select.deselect_all()
        # time.sleep(3)
        for option in select.options:
            print(option.text)

        self.driver.quit()

if __name__ == "__main__":
    case = TestCase()
    case.test_select()
"""
下拉菜单操作
select_by_value() 根据值进行选择
select_by_index() 根据索引进行进行选择
select_by_visible_text 根据文本选择
deselect_by_value 根据值反选
deselect_by_index 根据索引反选
deselect_by_visible_text 根据文本反选
deselect_all 反选所有
options 所有选项
all_selected_options 所有选中选项
first_selected_option 第一个选择选项
"""
