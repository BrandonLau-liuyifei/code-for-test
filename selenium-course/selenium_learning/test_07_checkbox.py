from selenium import webdriver
import time,os

class TestCase(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///"+path+"/test_07_checkbox.html"
        self.driver.get(file_path)
# 定位checkbox
    def test_checkbox(self):
        swimming = self.driver.find_element_by_name("swimming")
        if not swimming.is_selected():
             swimming.click()
        reading = self.driver.find_element_by_name("reading")
        if not reading.is_selected():
             reading.click()

        time.sleep(5)
        swimming.click()
        time.sleep(2)
        self.driver.quit()
# 定位radiobutton
    def test_radio(self):
        list = self.driver.find_elements_by_name("gender")
        # list[0].click()
        list[1].click()

if __name__ == "__main__":
    case = TestCase()
    # case.test_checkbox()
    case.test_radio()