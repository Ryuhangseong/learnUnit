import pytest

from page_object.login_page import LoginPage
from selenium import webdriver


class TestCases:
    def test_login(self):
        driver = webdriver.Chrome()
        text = 'LighClient'
        pwd = 'woaiwoziji134'
        lp = LoginPage(driver)
        lp.login(text, pwd)


if __name__ == '__main__':
    pytest.main(['-s'])
