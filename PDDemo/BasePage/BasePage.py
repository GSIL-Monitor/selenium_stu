"""
__author__ = 'LZL'
__mtime__ = '2018/7/24'
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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class BasePage:

    ''' 封装selenium常用方法，所有page类的基类 '''

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def _open_url(self, url):
        '''
        私有函数，打开指定url
        @param url: 指定url
        @return:null
        '''
        self.driver.get(url)
        self.driver.maximize_window()

    def open_url(self):
        '''
        对外暴露的打开指定url
        @return: null
        '''
        # self._open_url(self.base_url)
        self._open_url(self.base_url, self.pagetitle)

    def is_pagetitile(self, pagetitile):
        '''
        判断页面标题是否包含某字段
        @param pagetitile: 需判断的字段
        @return: True/False
        '''

        return pagetitile in self.driver.title

    def is_current_url(self, current_url):
        '''
        判断url是否包含某字段
        @param current_url: 需判断的url字段
        @return: True/False
        '''

        return current_url in self.driver.current_url

    def find_element(self, *loc):
        '''
        定位元素
        @param loc: 元组(定位元素的方法, 元素路径)
        @return: 定位成功的 元素
        '''

        try:
            # 要定位的元素加载进入dom并且在窗口显示范围内
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(loc[0], loc[1])
        except:
            # 这里应该是要改成记录在日志文件，并和测试报告发送到指定邮箱上的
            print("%s 页面中未能找到 %s元素"%(self, loc))

    def do_js(self, js):
        # 执行js
        self.driver.execute_script(js)


    def send_key(self, loc, value, do_clear=True, do_click=False):
        '''
        往定位元素输入值或者执行点击操作
        @param loc:  元组(定位元素的方法, 元素路径)
        @param value: 输入的值
        @param do_clear: 是否执行清除，默认True
        @param do_click: 是否执行点击，默认False
        @return:
        '''
        try:
            #获取对象object的属性或者方法，相当于实现了self.loc
            # loc = getattr(self, loc)
            if do_clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
            if do_click:
                self.find_element(*loc).click()
        except:
            # 这里应该是要改成记录在日志文件，并和测试报告发送到指定邮箱上的
            print("%s 页面中未能找到 %s元素" % (self, loc))

    def screen_shot(self, img_name, img_path='img'):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))