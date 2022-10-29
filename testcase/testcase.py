'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2022-10-27 20:04:50
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2022-10-29 12:26:22
FilePath: \learnUnit\testcase\testcase.py
Description: 

Copyright (c) 2022 by ryuhangseong liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

import unittest

from common.basemethod import *
from time import sleep
from ddt import ddt, data, unpack
from selenium.webdriver.common.keys import Keys
from common.param import *


@ddt
class TestBaidu:
    @data(*getdata())
    @unpack
    def testBaidu(self, searchWord, searchResult):
        openbrowser("https://www.sogou.com/")
        driver.find_element("id", "query").send_keys(searchWord)
        driver.find_element("id", "stb").click()
        sleep(2)
        responseText = driver.find_element("xpath",
                                           '//*[@id="sogou_vr_30010254_title_0"]/h3/span').text
        self.assertEqual(responseText, searchResult)
