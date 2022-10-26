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
        handle_all = self.driver.window_handles
        for handle in handle_all:
            if handle == handle_result_baidu:
                self.driver.switch_to.window(handle_index_baidu)
                break
            else:
                print("HANDLE GET WRONG!\n")
        self.driver.switch_to.window(handle_result_baidu)
        target = self.driver.find_element("id", "11")  # 需要将滚动条拖动至的指定的元素对象定位
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 将滚动条拖动到元素可见的地方
        sleep(2)
        print('\n')

    @file_data('./data/test_page_5_fsearch.yaml')
    def test_page_5_fsearch(self, **kwargs):
        fsearch = kwargs['fsearch']
        url = fsearch['url_fsearch']

    def test_page_6_iframe(self):
        url = "https://www.testclass.cn/test_html/iframe/frameset.html"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.switch_to.frame("rightframe")
        rightframe = self.driver.find_element("xpath", "/html/body/p")
        self.assertEqual(rightframe.text, "你喜欢做什么类型的软件测试?")
        self.driver.find_element("id", "security_test").click()
        self.driver.switch_to.frame("iframe_test")
        secondframe = self.driver.find_element("xpath", "/html/body/p")
        self.assertEqual(secondframe.text, "这只是一个测试用的Iframe页面")
        self.driver.switch_to.default_content()
        js_alert_hello = "alert('Hello World!');"
        self.driver.execute_script(js_alert_hello)
        sleep(2)
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Hello World!")

    def test_page_7_singlescroll(self):
        url = "https://www.testclass.cn/test_html/Sports_Single.html"
        self.driver.get(url)

        select = self.driver.find_element('name', 'Sports')
        all_options = select.find_elements("tag name", "option")
        for option in all_options:
            print("选项显示的文本：", option.text)
            print("选项值为：", option.get_attribute('value'))
            option.click()
            sleep(1)

        # 等待一下，演示效果；
        sleep(3)


if __name__ == '__main__':
    unittest.main()
