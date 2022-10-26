'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2022-10-22 19:26:21
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2022-10-22 19:35:49
FilePath: \learnUnit\test_sample.py
Description: 

Copyright (c) 2022 by ryuhangseong liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

import pytest

def func(x):
    return x + 1

def test_answer_right():
    assert func(3) == 4
    
def test_answer_wrong():
    assert func(3) == 5
    
class TestSample(object):
    @pytest.fixture()
    def count(self, request):
        print("init count")
        
        def fin():
            print("teardown count")
        request.addfinalizer(fin)
    
        return 10
    
    def test_answer_1(self, count):
        print("test_answer_1 get count: %s" % count)
        assert count == 10
    
    def test_answer_2(self, count):
        print("test_answer_2 get count: %s" % count)
        assert count == 10