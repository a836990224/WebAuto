# -*- coding = utf-8 -*-
# @Time : 2022/06/09 17:47
# @Author :Chilong
# @File : test_selenium.py
# @Software : PyCharm
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#unittest:写用例、执行用例、断言、生成报告
#要继承unittest.TestCase
class TestLogin(unittest.TestCase):
    #前置
    def setUp(self) -> None:
        # 选择一个浏览器来打开
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        self.driver.get("http://116.63.161.72:20080/#/login?redirect=%2Fdashboard")
    #后置
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
        pass

    #test_的函数代表一个测试用例
    def test_login_failed(self):
        #步骤
        # xpath定位元素,对元素进行输入操作
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input').send_keys("admin")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input').send_keys("111")
        # 按钮xpath定位,点击操作
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()
        #断言
        login = (By.XPATH,'/html/body/div[2]/p')
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(login))
        self.assertIn("用户名或密码错误",self.driver.find_element(*login).text)


if __name__ == '__main__':
    unittest.main()
