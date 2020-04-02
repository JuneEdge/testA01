# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://192.168.0.250:8001')
driver.find_element_by_css_selector(".log-content .login-view .login-form .el-input__inner").send_keys("15715859836")
driver.find_elements_by_class_name("el-input__inner")[1].send_keys("8888")
driver.find_element_by_css_selector(".log-content .login-view .login-form .reg .reg_btn").click()
driver.close()