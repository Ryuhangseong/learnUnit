import os

from sele_po.elementoperator import ElementOperator
from selenium.webdriver.common.by import By
path = os.path.dirname(os.path.abspath(__file__))


class BaiduAction(ElementOperator):
    def __init__(self):
        super(BaiduAction, self).__init__(self)
        self.url = "https://www.baidu.com"


if __name__ == '__main__':
    baidu = BaiduAction()
    baidu.open(baidu.url, 'chrome')
    baidu.close()
