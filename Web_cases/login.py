from selenium import webdriver
from selenium.webdriver.common.by import By

def login_in(driver, user, pw):
    #定位输入框并输入用户名、密码
    driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input').send_keys(user)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input').send_keys(pw)
    # 按钮xpath定位,点击操作
    driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()
