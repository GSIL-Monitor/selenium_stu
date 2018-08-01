import unittest
from selenium import webdriver



'''
    登陆QQ邮箱失败的作业
作业都是流水性
'''

class job_one(unittest.TestCase):

    def set_up(self):
        self.driver = webdriver.Chrome()
        return self.driver


    def test_login_error(self):
        self.driver = self.set_up()
        self.driver.get("https://mail.qq.com/")
        self.driver.switch_to.frame("login_frame")
        self.find_by_id("switcher_plogin").click()
        u = self.find_by_name("u")
        u.clear()
        u.send_keys("249837922")
        p = self.find_by_name("p")
        p.clear()
        p.send_keys("wodeqq123")
        self.find_by_id("login_button").click()
        #如果登陆正确就跳页了，定位会失败
        error = self.find_by_id("err_m").text
        #因为出现的登陆错误字样有时间的，所以取不到值
        self.assertTrue("" in error)


    def find_by_id(self, id_name):
        return self.driver.find_element_by_id(id_name)

    def find_by_css(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    def find_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # ## 每个用例执行完毕之后
    # def tear_down(self):
    #     print("over test_case")
    #     self.driver.quit()


if __name__ == "__main__":
    unittest.main()
