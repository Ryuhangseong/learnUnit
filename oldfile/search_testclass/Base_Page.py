from selenium import webdriver
from csv import reader

import unittest

class BasePage:
    
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
        
    def get_data(self):
        value_rows = []
        with open('./search_data.csv') as c:
            c_csv = reader(c)
            next(c_csv)
            for r in c_csv:
                value_rows.append(r)
        return value_rows