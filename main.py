import unittest

from common.basemethod import *
from time import sleep
from testcase.testcase import TestBaidu


class Search(unittest.TestCase, TestBaidu):

    @classmethod
    def setUpClass(cls) -> None:
        setimpwait(5)

    @classmethod
    def tearDownClass(cls) -> None:
        closebrowser()
        quitbrowser()


