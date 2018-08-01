import unittest
from BeautifulReport import BeautifulReport
import os
if __name__ == '__main__':
    # 项目路径
    base_path = os.path.dirname(os.path.realpath(__file__))
    # TestCase路径
    test_path = os.path.join(base_path, 'TestCase')

    test_suite = unittest.defaultTestLoader.discover(test_path, pattern='tes*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')
