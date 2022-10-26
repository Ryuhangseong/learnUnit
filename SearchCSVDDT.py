import csv
import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from time import sleep
from selenium.webdriver.common.keys import Keys


def get_data():
    value_rows = []
    with open('testdata.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
    return value_rows


@ddt
class SearchCSVDDT(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        url = "https://fsoufsou.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(2)

    @data(*get_data())
    @unpack
    def test_baidu(self, searchTerm, searchResult):
        driver = self.driver
        driver.find_element("id", "search-input").send_keys(searchTerm)
        driver.find_element("id", "search-input").send_keys(Keys.ENTER)
        sleep(2)
        responseText = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/a").text
        self.assertEqual(responseText, searchResult)


    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()