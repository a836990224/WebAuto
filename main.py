# -*- coding = utf-8 -*-
# @Time : 2022/06/09 17:47
# @Author :Chilong
# @File : test_selenium.py
# @Software : PyCharm
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#选择一个浏览器来打开
driver = webdriver.Chrome()
#窗口最大化
driver.maximize_window()

#'''登录操作'''
#打开一个网址
driver.get("http://116.63.161.72:20080/#/login?redirect=%2Fdashboard")
#隐式等待
driver.implicitly_wait(3)

'''登陆操作'''
#xpath定位元素,对元素进行输入操作
driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[2]/div/div/input').send_keys("admin")
driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[3]/div/div/input').send_keys("Root@feishu&2022")
#按钮xpath定位,点击操作
driver.find_element(By.XPATH,'//*[@id="app"]/div/form/button').click()

#'''点击布控预警'''
##显性等待
ele_bkyj = (By.XPATH,'//*[@id="app"]/div/section/div[2]/div[3]/div[1]/div[2]/div[4]')
WebDriverWait(driver,15).until(EC.visibility_of_element_located(ele_bkyj))
driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div[3]/div[1]/div[2]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/form/div[1]/div/div/input').send_keys("测试")
driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/form/div[2]/div/div/input').send_keys("江静")
driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/form/div[4]/div/button[1]').click()
time.sleep(2)
ele_zwsj = (By.XPATH,'//*[@id="app"]/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/div/span')
WebDriverWait(driver,10).until(EC.visibility_of_element_located((ele_zwsj)))
value_bukongyujing = driver.find_element(*ele_zwsj).text
if '暂无数据' in value_bukongyujing:
    print("用例1通过")
else:
    print("用例1失败")
#print(driver.title)

#‘’‘悬浮在运维服务上，点击设备管理’‘’
ac = ActionChains(driver)
ele_yunweifuwu = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[6]/div')
ac.move_to_element(ele_yunweifuwu).perform()
ele_shebeiguanli = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[6]/span/div/div[3]/span')
WebDriverWait(driver,15).until(EC.visibility_of_element_located(ele_shebeiguanli))
ele_shebeiguanli = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[6]/span/div/div[3]/span')
ac.click(ele_shebeiguanli).perform()

#鼠标左键点击设备名称/序列号的文本框并输入内容，点击搜索
time.sleep(2)
ele_shebeimingcheng = driver.find_element(By.XPATH,'//div[@id="app"]//div[@class="el-input el-input--medium"]//input[@class="el-input__inner"]')
ac.click(ele_shebeimingcheng.send_keys("21030013")).perform()
driver.find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/form/div[5]/div/button[1]').click()
ele_test = driver.find_elements(By.XPATH,'//*[@id="app"]/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/table/tbody')
ele_test_sbgl = ele_test[0].find_element(By.XPATH,'//*[@id="app"]/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div').text
if ele_test_sbgl  == "21030013":
    print("用例2通过")
else:
    print("用例2不通过")
#关闭页面
driver.close()

