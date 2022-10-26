# encoding:utf-8

import unittest


class TestDemo(unittest.TestCase):

    def demo(self, A, B, X):
        if A > 1 and B == 0:
            X = X / A
        if A == 2 or X > 1:
            X = X + 1
        return X

    def test_demo_with_conditional_coverage_1(self):
        '''
        使用条件覆盖测试 方法demo
        A=2，B=1，X=4
        '''
        X = self.demo(A=1, B=1, X=1)
        expected = 1
        self.assertEqual(expected, X)

    def test_demo_with_conditional_coverage_2(self):
        '''
        使用条件覆盖测试 方法demo
        A=-1，B=0，X=1
        '''
        X = self.demo(A=2, B=0, X=3)
        expected = 5/2
        self.assertEqual(expected, X)

if __name__ == '__main__':
    unittest.main()

