from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(BasePage):

    url = 'https://gitee.com/login'

    username = (By.NAME, 'user[login]')
    pwd = (By.NAME, 'user[password]')
    button = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[2]/div[1]/form[1]/div/div/div/div[4]/input')

    def login(self, text, pwd):
        self.open()
        self.input(self.username, text)
        self.input(self.pwd, pwd)
        self.click(self.button)
        self.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    text = 'LighClient'
    pwd = 'woaiwoziji134'
    lp = LoginPage(driver)
    lp.login(text, pwd)
