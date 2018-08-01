# 最新的测试报告包
from BeautifulReport import BeautifulReport
import unittest
import os
import time


class Beautiful_Report:

    def add_test_case(self, test_path, py_rule='test*_.py'):
        '''
        加载所有测试用例
        @param test_path: 测试用例所在目录
        @param py_rule: 测试py文件的正则
        @return: 加载完毕的测试用例
        '''
        tc_case = unittest.defaultTestLoader.discover(test_path, pattern=py_rule)
        return tc_case

    def do_report(self, test_suite, save_path, report_name='自动化测试报告', description='自动化测试报告'):
        '''
        运行测试套件，生成测试报告
        @param test_suite: 测试套件
        @param report_name: 测试报告名称，可带html可不带
        @param description: 测试报告注释
        @param save_path: 测试报告保存路径
        @return:
        '''
        report = BeautifulReport(test_suite)
        report.report(filename=report_name, description=description, log_path=save_path)


if __name__ == '__main__':
    # 项目路径
    base_path = os.path.dirname(os.path.realpath(__file__))
    # TestCase路径
    test_path = os.path.join(base_path, 'TestCase')
    # html测试报告路径
    report_path = os.path.join(base_path, 'report')

    report = Beautiful_Report()
    test_suite = report.add_test_case(test_path, py_rule='tc_sea*.py')
    report.do_report(test_suite, save_path=report_path)
