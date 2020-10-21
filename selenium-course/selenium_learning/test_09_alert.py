"""
弹框方式又3种
01 alert 用来提示
02 confirm 用来操作
03 prompt 输入内容
"""

from selenium import webdriver
import time,os

class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + "/test_09_alert.html"
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element_by_id("alert").click()
        #切换到alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        time.sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id("confirm").click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        # confirm.accept()
        time.sleep(3)
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element_by_id("prompt").click()
        time.sleep(5)
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        time.sleep(5)
        prompt.send_keys("50")
        prompt.accept()
        time.sleep(3)

if __name__ == "__main__":
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()


