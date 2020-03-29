__author__ = 'Administrator'
from selenium import webdriver
from time import sleep
from selenium_day3.user_login.def_user_login import login_by_different_username_password
from selenium_day3.change_password.def_change_password import change_password

browser = webdriver.Firefox()
login_by_different_username_password(browser,"sup","s1234567")
sleep(2)
change_password(browser,"s1234567","s12345678","s12345678")
sleep(2)
login_by_different_username_password(browser,"sup","s12345678")
sleep(2)
change_password(browser,"s12345678","s1234567","s1234567")
sleep(2)
browser.quit()
