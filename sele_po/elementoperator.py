import os
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# 引入chromedriver
chromedriver = "D:/Code/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver


class ElementOperator:

    def __init__(self, driver=None):
        """
        :param driver: 浏览器对象
        :return:
        """
        self.driver = driver

    def open(self, url, driver='chrome'):
        """
        :param driver: 浏览器对象
        :param url: 网址
        :return:
        """
        flag = False
        driver = driver.lower()
        if driver in ['chrome', 'edge']:
            try:
                socket.setdefaulttimeout(50)
                if driver == 'chrome':
                    # chrome_option.add_argument('--headless')
                    self.driver = webdriver.Chrome()
                self.driver.get(url)
                sleep(2)
            except Exception as e:
                print(e)
