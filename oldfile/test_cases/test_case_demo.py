import pytest

from page_object.login_page import LoginPage
from selenium import webdriver


class TestCases:
    def test_login(self, text, pwd):
        driver = webdriver.Chrome()
        lp = LoginPage(driver)
        lp.login(text, pwd)

    def test_login1(self):
        driver = webdriver.Chrome()
        text = 'LighClient'
        pwd = 'woaiwoziji134'
        lp = LoginPage(driver)
        lp.login(text, pwd)

if __name__ == '__main__':
    pytest.main(['-s'])
