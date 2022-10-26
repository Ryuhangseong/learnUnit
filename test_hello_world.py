import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './'#当前路径
discover = unittest.defaultTestLoader.discover(test_dir, pattern='login_success.py')#iot_*.py表示iot_开头的所有测试用例
fp = open("./test.html", "wb")#报告存放的路径
runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试用例情况:')
runner.run(discover)
fp.close()
