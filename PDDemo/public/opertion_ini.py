"""
__author__ = 'LZL'
__mtime__ = '2018/8/2'
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
from configparser import ConfigParser
import os


class operation_ini:
    ''' 对init文件的读操作 '''

    def __init__(self, ini_path):
        '''
        获取ini文件对象
        @param ini_path: ini文件绝对路径
        '''
        self.cp = ConfigParser()
        self.cp.read(ini_path)

    def get_sections(self):
        '''
        获得所有sections
        @return: 列表形式返回ini文件中所有的节
        '''
        return self.cp.sections()

    def get_options(self, section):
        '''
        获得指定节的所有参数中的键
        @param section:节名
        @return:列表形式返回指定节的所有参数键值对中的键
        '''
        return self.cp.options(section)

    def get_items(self, section):
        '''
         获得指定节的所有参数key-value
        @param section: 节名
        @return: 列表形式返回获得指定节的所有参数key-value,其中key-value是元组形式
        '''
        return self.cp.items(section)

    def get_value(self, section, option):
        '''
        获取指定节中指定参数中的value
        @param section: 节名
        @param option: 参数key
        @return: 参数value，返回string
        '''
        return self.cp.get(section, option)



# if __name__ == '__main__':
#     ini_path = os.path.join(os.path.dirname(os.getcwd()), 'File', 'test.ini')
#     file = operation_ini(ini_path)
#     sections = file.get_sections()
#     print(sections)
#     options = file.get_options('url')
#     print(options)
#     items = file.get_items('url')
#     print(items)
#     value = file.get_value('url','taobao_url')
#     print(value)