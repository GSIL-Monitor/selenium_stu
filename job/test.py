import unittest
from selenium import webdriver
# import time

class test(unittest.TestCase):

    def setUp(self): #每个用例执行之前执行
        print ('before test')
        self.dr = webdriver.Chrome()
        self.dr.get('http://localhost/wordpress/wp-login.php')

    def test_login(self):
        user_name = password = 'admin'
        self.by_id('user_login').send_keys(user_name)
        self.by_id('user_pass').send_keys(password)
        self.by_id('wp-submit').click()
        self.assertTrue('wp-admin' in self.dr.current_url)
        greeting_link = self.by_css('#wp-admin-bar-my-account .ab-item')
        self.assertTrue(user_name in greeting_link.text)

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def by_name(self, name):
        return self.dr.find_element_by_name(name)

    def tearDown(self): #每个用例执行之后
        print ('after every test')
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()
