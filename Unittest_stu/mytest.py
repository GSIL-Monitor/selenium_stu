# '''
#     假设有加减乘除四个测试用例
# '''
#
# import unittest
#
# class Add_Case(unittest.TestCase):
#     ''' 加法的测试 '''
#     def runTest(self): ##由于现在不需要加入到testsuite中，所有方法名字没用test开头
#         num_a = 10
#         num_b = 2
#         expect = 12
#         result = num_a + num_b
#         self.assertEqual(expect, result)
#
# class Sub_Case(unittest.TestCase):
#     ''' 减法的测试 '''
#     def runTest(self):
#         num_a = 10
#         num_b = 2
#         expect = 8
#         result = num_a - num_b
#         self.assertEqual(expect, result)
#
# class Div_Case(unittest.TestCase):
#     ''' 除法的测试 '''
#     def runTest(self):
#         num_a = 10
#         num_b = 2
#         expect = 5
#         result = num_a / num_b
#         self.assertEqual(expect, result)
#
# class Mul_Case(unittest.TestCase):
#     ''' 乘法的测试 '''
#     def runTest(self):
#         num_a = 10
#         num_b = 2
#         expect = 22
#         result = num_a * num_b
#         self.assertEqual(expect, result)
#
# if __name__ == '__mian__':
#     unittest.main()


'''
    提取开始时的相同代码进行优化：setUp()
    其实如果想优化，可以把self.assertEqual(expect, result)放在tearDown()中，但是怎么看都不合理...
'''

import unittest

class Operation(unittest.TestCase):

    def setUp(self):
        self.num_a = 10
        self.num_b = 2

    ''' 加法的测试 '''
    def test_add(self):
        expect = 12
        result = self.num_a + self.num_b
        self.assertEqual(expect, result)

    ''' 减法的测试 '''
    def test_sub(self):
        expect = 8
        result = self.num_a - self.num_b
        self.assertEqual(expect, result)

    ''' 除法的测试 '''
    def test_div(self):
        expect = 5
        result = self.num_a / self.num_b
        self.assertEqual(expect, result)

    ''' 乘法的测试 '''
    def test_mul(self):
        expect = 22
        result = self.num_a * self.num_b
        self.assertEqual(expect, result)

#
# if __name__ == '__mian__':
#     unittest.main()







