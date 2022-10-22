'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2022-10-19 10:40:27
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2022-10-20 19:09:53
FilePath: \learnUnit\test_search.py
Description: 

Copyright (c) 2022 by ryuhangseong liuhangcheng2002@gmail.com, All Rights Reserved. 
'''


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ddt import ddt, file_data

import unittest


@ddt
class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

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
        print('\n')

    def test_page_2_testclass(self):
        url_second = "https://www.testclass.cn/"
        self.driver.get(url_second)
        sleep(.5)
        self.driver.maximize_window()
        sleep(.5)
        self.driver.refresh()
        sleep(.5)
        self.driver.back()
        sleep(.5)
        self.driver.fullscreen_window()
        sleep(.5)
        self.driver.forward()
        sleep(.5)
        self.driver.set_window_rect(0, 0, 1024, 768)
        sleep(1)
        print('\n')

    @file_data("./data/test_page_3_baidu.yaml")
    def test_page_3_baidu(self, **kwargs):
        url_third = "https://www.baidu.com/"
        self.driver.get(url_third)
        self.assertEqual(self.driver.current_url, url_third)
        self.driver.maximize_window()
        print("\nMAXIMIZE OK!")
        baidu = kwargs['baidu']
        signin = self.driver.find_element(baidu['signin_method'], baidu['signin_path'])
        signin.click()
        print("SIGN IN OK!")
        signup = self.driver.find_element(baidu['signup_method'], baidu['signup_path'])
        window_index_handle = self.driver.current_window_handle
        signup.click()
        print("IFRAME OK!")
        window_all_handle = self.driver.window_handles
        self.assertEqual(window_all_handle[0], self.driver.current_window_handle)
        # print(window_all_handle)
        # print(self.driver.current_window_handle)
        self.driver.switch_to.window(window_all_handle[-1])
        loc_signup_button = (By.ID, "TANGRAM__PSP_4__submit")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc_signup_button))
        window_signup_handle = self.driver.current_window_handle
        self.driver.switch_to.window(window_index_handle)
        loc_index_iframe_close_button = (By.ID, "TANGRAM__PSP_4__closeBtn")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc_index_iframe_close_button))
        self.driver.find_element('id', 'TANGRAM__PSP_4__closeBtn').click()
        js_set_setting_visible = "document.getElementById('s-user-setting-menu').style.display='block';"
        js_set_setting_invisible = "document.getElementById('s-user-setting-menu').style.display='none';"
        sleep(2)
        self.driver.execute_script(js_set_setting_visible)
        sleep(2)
        self.driver.execute_script(js_set_setting_invisible)
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element('id', 's-usersetting-top')).perform()
        sleep(2)
        print('\n')

    @file_data('./data/test_page_4_huawei.yaml')
    def test_page_4_huawei(self, **kwargs):
        huawei = kwargs['huawei']
        url_baidu = huawei['url_baidu']
        loc_baidu_search_button = (By.ID, "su")
        loc_baidu_search_input = (By.ID, "kw")
        loc_baidu_result_container = (By.ID, "container")
        self.driver.get(url_baidu)
        self.driver.minimize_window()
        self.assertEqual(self.driver.current_url, huawei['url_baidu'])
        self.driver.set_window_position(125, 125)
        self.driver.set_window_size(800, 600)
        self.driver.set_window_rect(0, 0, 1152, 864)
        self.driver.maximize_window()
        self.driver.fullscreen_window()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc_baidu_search_button))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc_baidu_search_input))
        handle_index_baidu = self.driver.current_window_handle
        title_index_baidu = self.driver.title
        self.driver.find_element("id", "kw").send_keys("华为")
        self.driver.find_element("id", "su").click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc_baidu_result_container))
        self.driver.back()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc_baidu_search_button))
        title_index_baidu_back = self.driver.title
        self.assertEqual(title_index_baidu, title_index_baidu_back)
        self.driver.forward()
        handle_result_baidu = self.driver.current_window_handle
        print('\n')


if __name__ == '__main__':
    unittest.main()
