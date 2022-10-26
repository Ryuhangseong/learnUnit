from lib2to3.pgen2 import driver
from selenium import webdriver


import unittest

class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        
    def open_page(self):
        self.driver.get(self.url)
        
    def close_page(self):
        self.driver.close()
        
    def quit_browser(self):
        self.driver.quit()
        
    def locator(self, loc):
        return self.driver.find_element(*loc)
    
    def send_info(self, loc, text):
        self.driver.locator(loc).send_keys(text)
        
    def send_click(self, loc):
        self.driver.locator(loc).click()