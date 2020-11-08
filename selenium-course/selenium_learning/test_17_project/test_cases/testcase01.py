def test_01():
    print("hahaha")

from selenium import webdriver
import pyautogui,time

def test_02():
    driver = webdriver.Chrome()
    driver.get("http://www.jpress.io/user/register")
    driver.maximize_window()
    time.sleep(1)
    element = driver.find_element_by_id("agree")
    rect = element.rect
    pyautogui.click(rect["x"],rect["y"])
    # element.click()
    time.sleep(3)

"""
PyAutoGUI 模块
pyautogui.positon()   确定鼠标当前位置
pyautogui.moveTo(x,y[,duration=t])  移动
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.click()
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()  点击
pyautogui.dragTo(x,y[,duration=t]) 拖动
pyautogui.typewrite(s[,duration=0]) 控制键盘
"""

