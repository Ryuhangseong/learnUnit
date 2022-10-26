import time
import unittest

from time import sleep
from selenium import webdriver
from ddt import ddt, data, unpack, file_data


@ddt
class CasesDemo(unittest.TestCase):

    # 前置条件
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        url = 'https://www.baidu.com'
        self.driver.get(url)

    # 后置条件
    def tearDown(self) -> None:
        self.driver.quit()

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Chrome()
    #     url = 'https://www.baidu.com'
    #     cls.driver.get(url)

    # @data(['kw', '妖梦'], ['kw', '东方project'])
    # @unpack
    @file_data('../data/user.yaml')
    def test_1(self, **kwargs):
        input_ = kwargs['input']
        button = kwargs['button']
        self.driver.find_element(input_['name'], input_['value']).send_keys(input_['text'])
        self.driver.find_element(button['name'], button['value']).click()
        sleep(2)

    # def test_2(self):
    #     self.driver.find_element('id', 'kw').clear()
    #     self.driver.find_element('id', 'kw').send_keys('妖梦')
    #     self.driver.find_element('id', 'su').click()
    #     sleep(2)
    #
    # def test_3(self):
    #     self.driver.find_element('id', 'kw').clear()
    #     self.driver.find_element('id', 'kw').send_keys('东方project')
    #     self.driver.find_element('id', 'su').click()
    #     sleep(2)


if __name__ == '__main__':
    unittest.main()
