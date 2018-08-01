"""
__author__ = 'LZL'
__mtime__ = '2018/7/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


import unittest
# 注意要定位到类进行导入，因为下面是直接使用类进行操作，更方便
from PDDemo.Page.Search_Page import Search_Page
from BeautifulReport import BeautifulReport
from selenium import webdriver
from time import sleep


class Search_Case(unittest.TestCase):
    '''百度搜索测试用例'''

    ## 使用优化过后的测试报告,需要使用:https://blog.csdn.net/maybe_frank/article/details/79352097
    @classmethod
    def setUpClass(cls):
        # 准备环境
        cls.driver = webdriver.Chrome()
        # 对测试用例的元素定位进行隐式等待
        cls.driver.implicitly_wait(20)
        cls.url = "http://www.baidu.com"
        cls.content_one = "Python3"
        cls.content_two = "中国"
        cls.content_three = "Python"

    @BeautifulReport.add_test_img('测试成功.png')
    def test_one(self):
        ''' 英文+数字的内容搜索 '''
        search_page = Search_Page(self.driver, self.url)
        search_page.open()
        search_page.search_content(self.content_one)
        search_page.button_click()
        self.assertTrue(search_page.is_success(self.content_one))

    @BeautifulReport.add_test_img('测试失败.png')
    def test_two(self):
        ''' 中文的内容搜索 '''
        search_page = Search_Page(self.driver, self.url)
        search_page.open()
        search_page.search_content(self.content_two)
        search_page.button_click()
        self.assertTrue(search_page.is_success(self.content_two))

    @BeautifulReport.add_test_img('test2.png')
    def test_three(self):
        ''' 英文的内容搜索 '''
        search_page = Search_Page(self.driver, self.url)
        search_page.open()
        search_page.search_content(self.content_three)
        search_page.button_click()
        # self.driver.get_screenshot_as_file(r"E:\git_lzl\Selenium_Demo\PDDemo\TestCase\img\test2.png")
        # BeautifulReport.add_test_img(r"E:\git_lzl\Selenium_Demo\PDDemo\TestCase\img\test2.png")
        self.assertTrue(search_page.is_success(self.content_three))





    ## 如SetUp
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
