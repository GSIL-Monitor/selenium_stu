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

import os
import unittest
# 注意要定位到类进行导入，因为下面是直接使用类进行操作，更方便
from PDDemo.Page.Search_Page import Search_Page
from BeautifulReport import BeautifulReport
from selenium import webdriver


class Search_Case(unittest.TestCase):
    '''百度搜索测试用例'''

    def save_img(self, img_name):
        """
        ## 为了让BeautifulReport进行自动的失败截图，必须在测试类定义该save_img方法
          传入一个img_name, 并存储到默认的文件路径下：当前项目的img文件夹，必须存在该文件夹！！
        :param img_name: 图片名称，无需后缀
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('img'), img_name))
        # 封装了截图方法到别的类然后进行调用的话，无法进行失败截图。可能是BeautifulReport进行了限制
        # 和上面的img文件夹一样，如有需要，可以去源码进行更改
        # Search_Page.screen_shot(img_name, img_path)

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

    # 注意，截图名称要和方法名称一致，否则报告生成的图片路径找不到
    @BeautifulReport.add_test_img('test_one')
    def test_one(self):
        ''' 英文+数字的内容搜索 '''
        search_page = Search_Page(self.driver, self.url)
        search_page.open()
        search_page.search_content(self.content_one)
        search_page.button_click()
        self.assertTrue(search_page.is_success(self.content_one))

    @BeautifulReport.add_test_img('test_two')
    def test_two(self):
        ''' 中文的内容搜索 '''
        search_page = Search_Page(self.driver, self.url)
        search_page.open()
        search_page.search_content(self.content_two)
        search_page.button_click()
        self.assertTrue(search_page.is_success(self.content_two))

    @BeautifulReport.add_test_img('test_three')
    def test_three(self):
        ''' 英文的内容搜索 '''
        search_page = Search_Page(self.driver, self.url)
        search_page.open()
        search_page.search_content(self.content_three)
        search_page.button_click()
        self.assertTrue(search_page.is_success(self.content_three))

    ## 如SetUp
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# if __name__ == "__main__":
#     unittest.main()
