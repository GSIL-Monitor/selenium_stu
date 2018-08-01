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


from PDDemo.BasePage.BasePage import BasePage
from selenium.webdriver.common.by import By


class Search_Page(BasePage):
    # 百度的查询页面，继承了BasePage

    # 所要定位的元素
    search_ele = (By.ID, "kw")
    button_ele = (By.ID, "su")

    def open(self):
        # 重写父类BasePage的open方法
        self._open_url(self.base_url)

    def search_content(self, content_value):
        # 对搜索框进行定位和输入搜索内容，调用父类方法
        self.send_key(value=content_value, do_clear=True, do_click=False, loc=self.search_ele)

    def button_click(self):
        # 对搜索按键进行定位和点击，调用父类方法
        Search_Button = self.find_element(*self.button_ele)
        Search_Button.click()

    def is_success(self, current_url):
        return self.is_current_url(current_url)