from selenium import webdriver
import  time
import os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+"/test_06_formdata.html"
        print(file_path)
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element_by_id("username")
        username.send_keys("liuyifei")
        print(username.get_attribute("value"))
        password = self.driver.find_element_by_id("pwd")
        password.send_keys("123")
        print(password.get_attribute("value"))

        time.sleep(2)
        self.driver.find_element_by_id("submit").click()

        self.driver.switch_to.alert.accept()
        time.sleep(2)

        username.clear()
        password.clear()

if __name__ == "__main__":
    case=TestCase()
    case.test_login()