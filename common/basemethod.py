'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2022-10-27 20:20:40
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2022-10-29 11:12:18
FilePath: \learnUnit\common\basemethod.py
Description: 

Copyright (c) 2022 by ryuhangseong liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

from csv import reader
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


def setimpwait(time):
    return driver.implicitly_wait(time)


def openbrowser(url):
    return driver.get(url)


def maxwin():
    return driver.maximize_window()


def minwin():
    return driver.minimize_window()


def setrect(x, y, width, height):
    return driver.set_window_rect(x, y, width, height)


def gethandle():
    return driver.current_window_handle


def getallhandle():
    return driver.window_handles


def runjs(js):
    return driver.execute_script(js)


def getdata():
    value_rows = []
    with open('D:\\code\\python\\learnUnit\\data\\data.csv', encoding='utf-8') as c:
        c_csv = reader(c)
        next(c_csv)
        for row in c_csv:
            value_rows.append(row)
    return value_rows


def closebrowser():
    return driver.close()


def quitbrowser():
    return driver.quit()


def findele(*loc):
    return driver.find_element(loc)


def findeles(*loc):
    return driver.find_elements(loc)


def clcele(*loc):
    return findele(loc).click()


def sendele(*loc, text):
    return findele(loc).send_keys(text)


def setectimevis(timeout, poll_frequency, *loc):
    return WebDriverWait(driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))


def setectimeclc(timeout, poll_frequency, *loc):
    return WebDriverWait(driver, timeout, poll_frequency).until(EC.element_to_be_clickable(loc))


def acceptalert():
    return driver.switch_to.alert.accept()


def disalert():
    return driver.switch_to.alert.dismiss()


