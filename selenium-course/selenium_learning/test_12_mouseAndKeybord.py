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
click(on_element=None)   单击鼠标左键
click_and_hold(on_element=None)  点击鼠标左键，不松开
context_click(on_element=None) 单击鼠标右键
double_click(on_element=None)  双击鼠标左键
drag_and_drop(source,target)  拖拽刀到某个元素后松开
drag_and_drop_by_offset(source,xoffset,yoffset)  拖拽到某个坐标后松开
move_to_element()  鼠标移动到某个元素
move_by_offset(xoffset,yoffset)  鼠标从当前位置移动到某个坐标
move_to_element_with_offset(to_element,xoffset,yoffset)  鼠标移动到举例某个元素左上坐标多少的举例
perform()  执行链中的所有动作
release(on_element=None)  在某个元素位置松开鼠标左键
键盘操作
key_down(value,on_element=none)  按下某个键盘上的按键
key_up(value,element=none) 松开某个键
send_keys(*keys_to_send) 发送某个键到当前焦点到元素
send_keys_to_element(element,*keys_to_send) 发送某个键到指定元素
"""

