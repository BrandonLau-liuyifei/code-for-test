__author__ = 'Administrator'
from time import sleep
from selenium_day3.shijianchuo.def_shijianchuo import jietu
# 定义函数，实现修改密码的过程，将旧密码、新密码、确认密码当做参数传入
def change_password(browser,oldpassword,newpassword,passwordagain):
    try:
        browser.find_element_by_xpath('//a[@title="密码修改"]').click()
        sleep(2)
        # 输入旧密码，需要切入框架，先定位框架
        iframe_element = browser.find_element_by_xpath('//iframe[contains(@src,"/oa/common/tools/updatePassword.jsp?uuid=")]')
        browser.switch_to.frame(iframe_element)
        browser.find_element_by_xpath('//input[@id="oldpassword"]').send_keys(oldpassword)
        sleep(2)
        browser.find_element_by_xpath('//input[@id="newpassword"]').send_keys(newpassword)
        sleep(2)
        browser.find_element_by_xpath('//input[@id="passwordagain"]').send_keys(passwordagain)
        # 点击保存按钮
        browser.find_element_by_xpath('//button[@id="button_save"]').click()
        # 操作完成后切出到默认框架
        browser.switch_to.default_content()
    except Exception as e:
        jietu(browser,"修改密码报错")
        raise e