"""
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2022-10-19 10:40:27
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2022-10-20 11:00:55
FilePath: \learnUnit\test_search.py
Description:

Copyright (c) 2022 by ryuhangseong liuhangcheng2002@gmail.com, All Rights Reserved.
"""

from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from ddt import ddt, file_data

import unittest


@ddt
class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    @file_data("./data/test_page_1_gitee.yaml")
    def test_page_1_gitee(self, **kwargs):
        url_first = "https://gitee.com/"
        self.driver.get(url_first)
        self.driver.maximize_window()
        handle_window_index = self.driver.current_window_handle
        self.assertEqual(self.driver.current_url, url_first)
        signup = kwargs['signup']
        signup_button = self.driver.find_element(signup['way'], signup['path'])
        ActionChains(self.driver).move_to_element(signup_button).key_down(Keys.CONTROL).click().key_up(
            Keys.CONTROL).perform()
        handle_all_windows = self.driver.window_handles
        for handle in handle_all_windows:
            if handle != handle_window_index:
                self.driver.switch_to.window(handle)
                print("Now Register Window!")
                sleep(2)

    # def test_page_2_testclass(self):
    #     url_second = "https://www.testclass.cn/"
    #     self.driver.get(url_second)
    #     sleep(.5)
    #     self.driver.maximize_window()
    #     sleep(.5)
    #     self.driver.refresh()
    #     sleep(.5)
    #     self.driver.back()
    #     sleep(.5)
    #     self.driver.fullscreen_window()
    #     sleep(.5)
    #     self.driver.forward()
    #     sleep(.5)
    #     self.driver.set_window_rect(0, 0, 1024, 768)
    #     sleep(1)


if __name__ == '__main__':
    unittest.main()
