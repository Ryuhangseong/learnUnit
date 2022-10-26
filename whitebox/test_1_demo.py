# encoding:utf-8

import unittest


class TestDemo(unittest.TestCase):

    def demo(self, A, B, X):
        if A > 1 and B == 0:
            X = X / A
        if A == 2 or X > 1:
            X = X + 1
        return X

    def test_demo_with_statement_coverage(self):
        """
        使用语句覆盖测试 方法demo
        输入：A=2，B=0，X=3
        预期结果：X = 2.5
        """
        X = self.demo(A=2, B=0, X=3)
        self.assertEqual(2.5, X)


if __name__ == '__main__':
    unittest.main()