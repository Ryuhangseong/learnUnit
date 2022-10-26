# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from ddt import ddt, data, unpack
# from Base_Page import BasePage
#
#
# import unittest
#
# @ddt
# class test_fsearch(BasePage):
#
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#
#     def tearDown(self) -> None:
#         quit_browser()
#
#     @data(*get_data())
#     @unpack
#     def test_1_testclass(self, url):
#         driver = self.driver
#         driver.open_page(url)
#         self.assertEqual(url, driver.current_url)
#         WebDriverWait(driver, 0.5, 5).until(EC.title_is("F 搜"))
#         handle_search = driver.current_window_handle
#
#
# if __name__ == '__main__':
#