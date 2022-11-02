# -*- coding: utf-8 -*-
# @Time     :2022/11/2 19:53
# @Author   :liu hangcheng
# @Email    :liuhangcheng2002@gmail.com
# @File     :elementoperator.py

import base64
import os
import random
import socket
import time
import yaml
from PIL import Image
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from appium import webdriver as app_webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Locator:
    def __init__(self, element, wait_sec=3, by_type='id', locator_name='', desc=''):
        """

        :param element:定位语句
        :param wait_sec:等待时间，默认3秒
        :param by_type:定位方式
        :param locator_name:变量名
        :param desc:描述
        """
        self.element = element
        self.wait_sec = wait_sec
        self.by_type = by_type
        self.locator_name = locator_name
        self.desc = desc

    def __str__(self):
        return f'{self.desc}:(By:{self.by_type},element:{self.element})'

    def __repr__(self):
