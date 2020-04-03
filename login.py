# coding:utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import unittest
import time
import requests
import json


class fzman(unittest.TestCase):
    '''登录页面'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://192.168.0.250:8001/web"

    def test_login(self):
        '''手机号、验证码为空'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector(".log-content .login-view .login-form .reg .reg_btn").click()

    def test_login2(self):
        '''手机号、验证码不匹配'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector(".log-content .login-view .login-form .el-input__inner").send_keys("15715859836")
        driver.find_elements_by_class_name("el-input__inner")[1].send_keys("1234")
        driver.find_element_by_css_selector(".log-content .login-view .login-form .reg .reg_btn").click()



    def test_login3(self):
        '''手机号、验证码匹配'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector(".log-content .login-view .login-form .el-input__inner").send_keys("15715859836")
        driver.find_elements_by_class_name("el-input__inner")[1].send_keys("8888")
        driver.find_element_by_css_selector(".log-content .login-view .login-form .reg .reg_btn").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":

    testunit = unittest.TestSuite()
    testunit.addTest(fzman("test_login"))
    testunit.addTest(fzman("test_login2"))
    testunit.addTest(fzman("test_login3"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    filename = './' + now + 'result.html'

    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='纺织超人登录报告',
                            description='用例执行情况：')

    runner.run(testunit)  # 允许测试用例
    fp.close()      # 关闭报告文件













