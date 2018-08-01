from PDDemo.report import HTMLTestRunner_jpg
import unittest
import os
import time

# 项目所处的路径
# 这两种方法有区别的：https://blog.csdn.net/cyjs1988/article/details/77839238

# 1.获得刚才所引用的模块 所在的绝对路径;__file__为内置属性
obj_path = os.path.dirname(os.path.realpath(__file__))
# # 2.去掉当前所运行的脚本的文件名，返回目录
# obj_path = os.getcwd()

# 测试用例的存放路径
test_path = os.path.join(obj_path, "TestCase")
# 测试报告的存放路径
report_path = os.path.join(obj_path, "report", 'html')

class RunTest():



    def creat_suite(self):
        ''' 加载测试套件 '''
        # 一次性添加指定目录下的测试文件的测试用例；但是添加规则是按照ASCAII码的顺序进行添加，test后的名称
        tc_case = unittest.defaultTestLoader.discover(start_dir=test_path, pattern="tc*.py", top_level_dir=None)
        return tc_case

    def do_report(self):
        ''' 生成测试报告 '''

        # 测试报告的名称；时间中间不能用:隔开，会生成不了对应的文件
        now_time = time.strftime('%Y-%m-%d', time.localtime())
        report_name = "\\" + now_time + "-report.html"

        # 生成测试报告
        report = HTMLTestRunner_jpg.HTMLTestRunner(
            title="测试报告",
            description=report_name,
            # 打开文件，二进制写入
            stream=open(report_path + report_name, "wb"),
            # 用例失败重跑
            # retry=1,
            # 控制台输出测试用例运行情况的风格
            verbosity=2
        )
        # 获取加载好的TestSuite
        report.run(self.creat_suite())

# if __name__ == "__main__":
#     # 测试，调用生成报告类并执行测试
#     RunTest().do_report()


