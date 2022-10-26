from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_source(self):
        return self.driver.page_source

    def accept_alert(self):
        wait = WebDriverWait(self.driver, 10, 0.5)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert


class LoginPage(object):
    url = "http://a.4399en.com/"

    def __init__(self, driver):
        self.driver = driver

    def login(self, user, pwd):
        self.driver.get(LoginPage.url)
        self.driver.find_element(By.XPATH, "/html/body/header/a[3]").click()

        wait = WebDriverWait(self.driver, 20, 0.5)
        account = wait.until(EC.visibility_of_element_located((By.ID, "modify-account")))
        account.clear()
        account.send_keys(user)

        password = self.driver.find_element(By.ID, "modify-password")
        password.clear()
        password.send_keys(pwd)

        self.driver.find_element(By.XPATH, "//input[@type='submit'][@value='Login']").click()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument(
        'User-Agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    driver = webdriver.Chrome(options=options)
    login_page = LoginPage(driver)
    login_page.login("gfc@qq.com", "123456")
    login_page.quit()
