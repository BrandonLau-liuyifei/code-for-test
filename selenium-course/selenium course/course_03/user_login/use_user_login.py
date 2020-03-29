__author__ = 'Administrator'
from selenium import webdriver
from selenium_day3.user_login import def_user_login
from time import sleep

browser = webdriver.Firefox()
# def_user_login.login_sup(browser)
def_user_login.login_by_different_username_password(browser,"sup","s1234567")
sleep(2)
def_user_login.login_by_different_username_password(browser,"supppppp","s1234567")
sleep(2)
browser.quit()