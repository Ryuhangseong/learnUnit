import os
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# 引入driver
chromedriver = str(os.getcwd().replace("\\test", "") + "\\driver\\chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chromedriver
msedgedriver = str(os.getcwd().replace("\\test", "") + "\\driver\\msedgedriver.exe")
os.environ["webdriver.edge.driver"] = msedgedriver


class ElementOperator:

    def __init__(self, driver=None):
        """
        :param driver: 浏览器对象
        :return:
        """
        self.driver = driver

    def open(self, url, driver='chrome'):
        """
        :param driver: 浏览器对象，默认为chrome
        :param url: 网址
        :return: 打开浏览器
        """
        flag = False
        driver = driver.lower()
        if driver in ['chrome', 'edge']:
            try:
                socket.setdefaulttimeout(50)
                if driver == 'chrome':
                    # chrome_option.add_argument('--headless')
                    self.driver = webdriver.Chrome(chromedriver)
                if driver == 'edge':
                    # edge_option.add_argument('--headless')
                    self.driver = webdriver.Edge(msedgedriver)
                self.driver.implicitly_wait(10)
                self.driver.get(url)
                try:
                    self.driver.maximize_window()
                except Exception as e:
                    print(f"浏览器最大化失败：{e}")
                flag = True
            except Exception as e:
                raise Exception(e)
            if not flag:
                raise EC.WebDriverException(f"打开浏览器进入{url}失败")
        return self.driver

    def close(self):
        """
        :return: 关闭浏览器
        """
        if self.driver:
            try:
                self.driver.close()
            except Exception as e:
                print(f"close浏览器失败：{e}")
            try:
                self.driver.quit()
            except Exception as e:
                print(f"quit浏览器失败：{e}")

    def click(self, locator, many=False, num=0):
        if many:
            ele = self.find_elements(locator)[num]
        else:
            ele = self.find_element(locator)
        print(f"点击「{locator.desc}」")
        ele.click()
        time.sleep(0.2)