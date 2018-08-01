'''
    封装webdriver的方法，更方便调用
'''
from selenium import webdriver


class basic_webdriver:

    '''
        获取webdriver
    '''
    def set_up(self, driver_name):
        self.driver = webdriver.Chrome()
        return self.driver

    def find_by_id(self, id_name):
        return self.driver.find_element_by_id(id_name)

    def find_by_css(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    def find_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    ## 每个用例执行完毕之后
    def tear_down(self):
        print("over test_case")
        self.driver.quit()



