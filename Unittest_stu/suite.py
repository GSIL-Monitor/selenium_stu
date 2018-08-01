import unittest
from Unittest_stu import mytest

''' 
    TestSuite：加载想要执行的TestCase并运行，把结果返回给TestResult
               或者直接TextTestRunner()运行
'''


'''
    TestSuite加载Operation类的所有测试方法
'''
def operation_suite():
    Operation = mytest.Operation
    operation_suite = unittest.makeSuite(Operation)
    runner = unittest.TextTestRunner()
    runner.run(operation_suite)

'''
     TestSuite加载Operation类的add和div方法
'''

def add_div_suite():
    Operation = mytest.Operation
    my_suite = unittest.TestSuite()
    # 记住语法
    my_suite.addTest(Operation("test_add"))
    my_suite.addTest(Operation("test_div"))
    runner = unittest.TextTestRunner()
    runner.run(my_suite)

'''
    运行
'''
if __name__ == '__main__':
    # add_div_suite()
    operation_suite()
