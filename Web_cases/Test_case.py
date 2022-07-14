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
from Web_cases import login
import pyautogui

#unittest:写用例、执行用例、断言、生成报告
#要继承unittest.TestCase
class Testlogin(unittest.TestCase):
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

    def test_login_success(self):
        # xpath定位元素,对元素进行输入操作
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input').send_keys("admin")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input').send_keys("Root@feishu&2022")
        # 按钮xpath定位,点击操作
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()
        #断言
        title = (By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[1]/div/span[2]')
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(title))
        self.assertEqual("admin",self.driver.find_element(*title).text)


class Test_shujujiansuo(unittest.TestCase):
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

    #测试用例
    def test_sjjs_tongji_success(self):
        #引入登录模块
        login.login_in(self.driver,"admin","Root@feishu&2022")
        # xpath定位元素，对元素进行点击操作，跳转页面
        ele_sjjs = (By.XPATH,'//*[@id="app"]/div/section/div[2]/div[3]/div[1]/div[2]/div[1]/span')
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(ele_sjjs))
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div[3]/div[1]/div[2]/div[1]/span').click()
        time.sleep(2)
        # 先左键点击，右键选择小方框，出现区域统计，进行点击
        ac = ActionChains(self.driver)
        youjian_gouxuankuang = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div/div/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')
        ac.click(youjian_gouxuankuang).perform()
        ac.context_click(youjian_gouxuankuang).perform()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div[2]/div[1]').click()
        #断言
        tongji_yemian_title = (By.XPATH,'//*[@id="app"]/div/section/div[2]/div/div/div[2]/div[1]/div/span')
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(tongji_yemian_title))
        self.assertEqual("数据分析", self.driver.find_element(*tongji_yemian_title).text)

    def test_sjjs_tongji_guiji_success(self):
        #引入登录模块
        login.login_in(self.driver,"admin","Root@feishu&2022")
        # xpath定位元素，对元素进行点击操作，跳转页面
        ele_sjjs = (By.XPATH,'//*[@id="app"]/div/section/div[2]/div[3]/div[1]/div[2]/div[1]/span')
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(ele_sjjs))
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div[3]/div[1]/div[2]/div[1]/span').click()
        time.sleep(2)
        # 先左键点击，右键选择小方框，出现统计，进行点击
        ac = ActionChains(self.driver)
        youjian_gouxuankuang = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div/div/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')
        ac.click(youjian_gouxuankuang).perform()
        ac.context_click(youjian_gouxuankuang).perform()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div[2]/div[1]').click()
        #等待新页面出现，点击新页面小方框，
        time.sleep(1)
        self.driver.implicitly_wait(3)
        sjjs_tongji_guiji = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[1]/div/label/span/span')
        ac.click(sjjs_tongji_guiji).perform()
        ac.context_click(sjjs_tongji_guiji).perform()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div[2]/div[2]').click()
        #断言
        guiji_yemian_title = (By.XPATH,'//*[@id="app"]/div/section/div[2]/div[3]/div/div[1]/div')
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(guiji_yemian_title))
        self.assertEqual("信息1",self.driver.find_element(*guiji_yemian_title).text)

if __name__ == '__main__':
    unittest.main()
