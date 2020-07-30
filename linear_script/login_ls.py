'''登录'''
from appium import webdriver
import unittest
from selenium.webdriver.common.by import By

'''打开每日优鲜'''
desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'cn.missfresh.application',
    'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
    'unicodeKeyboard': True,  # 开启Unicode输入法，保证输入稳定
    'resetKeyboard': True,  # unicode输入结束后，重置输入法
    'newCommandTimeout': 600,  # appium服务等待发送新消息的时间
    'noReset': True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)

'''控件定位'''
loc_my = (By.ID, 'cn.missfresh.application:id/mineTab')  # 我的
loc_login_sign = (By.ID, 'cn.missfresh.application:id/tv_nickname')  # 登录
loc_phone = (By.ID, 'cn.missfresh.application:id/phoneNumber_et')  # 手机号
loc_get_check_code = (By.ID, 'cn.missfresh.application:id/getCheckCode')  # 获取验证码按钮
loc_check_code = (By.ID, 'cn.missfresh.application:id/checkCode_et')  # 验证码
loc_deal = (By.ID, 'cn.missfresh.application:id/iv_protocol')  # 勾选协议
loc_click_login = (By.ID, 'cn.missfresh.application:id/btn_login')  # 登录按钮
loc_assert = (By.ID, 'cn.missfresh.application:id/tv_nickname')  # 断言

'''参数'''
phone = '18380251182'

'''实现步骤'''
driver.find_element(*loc_my).click()  # 点击我的
print('点击我的')
driver.find_element(*loc_login_sign).click()  # 点击登录/注册
print('点击登录/注册')
driver.find_element(*loc_phone).send_keys(phone)  # 输入手机号
print('输入手机号')
driver.find_element(*loc_get_check_code).click()  # 点击获取验证码
print('点击获取验证码')
check_code = input('请输入验证码：')
driver.find_element(*loc_check_code).send_keys(check_code)  # 输入验证码
print('输入验证码')
driver.find_element(*loc_deal).click()  # 勾选协议
print('勾选协议')
driver.find_element(*loc_click_login).click()  # 点击登录
print('点击登录')
text = driver.find_element(*loc_assert).text  # 获取断言
print('获取断言')
unittest.TestCase().assertEqual('小鲜', text)  # 断言

driver.quit()
print('退出')
