'''新增收货地址'''
import time
import unittest
from appium import webdriver
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
loc_my = (By.ID,'cn.missfresh.application:id/mineTab')  # 我的
loc_click_address = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]')  # 【收货地址】定位
loc_click_add_address = (By.ID,'cn.missfresh.application:id/btn_add_address')  # 【新增收货地址】定位
loc_receiver = (By.ID,'cn.missfresh.application:id/et_edit_address_receiver')  # 收货人定位
loc_sir = (By.ID,'cn.missfresh.application:id/rg_sex_sir')  # 先生
loc_tel = (By.ID,'cn.missfresh.application:id/et_edit_address_tel')  # 手机号码
loc_click_choose = (By.ID,'cn.missfresh.application:id/tv_edit_detail_address')  # 收货地址输入框
loc_keyword = (By.ID,'cn.missfresh.application:id/et_search_address_input')  # 关键字
loc_choose = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout')  # 选择地址
loc_doorplate = (By.ID,'cn.missfresh.application:id/et_edit_doorplate')  # 楼号门牌
loc_tag = (By.ID,'cn.missfresh.application:id/rb_company_address_tags')  # 公司标签
loc_default_address = (By.ID,'cn.missfresh.application:id/ssb_default_address_switch')  # 设置默认地址
loc_save = (By.ID,'cn.missfresh.application:id/btn_save_address')  # 保存收获地址
loc_assert = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]')  # 断言

'''参数'''
receiver = '李白'
tel = '18380251182'
keyword = '香山'
doorplate = '701'

'''实现步骤'''
driver.find_element(*loc_my).click()  # 点击我的
print('点击我的')
driver.find_element(*loc_click_address).click()  # 点击收货地址
print('点击收货地址')
driver.find_element(*loc_click_add_address).click()  # 点击新增收货地址
print('点击新增收货地址')
driver.find_element(*loc_receiver).clear()  # 清空收货人
driver.find_element(*loc_receiver).send_keys(receiver)  # 输入收货人
print('输入收货人')
driver.find_element(*loc_sir).click()  # 性别选择先生
print('性别选择先生')
driver.find_element(*loc_tel).clear()  # 清空手机号
driver.find_element(*loc_tel).send_keys(tel)  # 输入手机号
print('输入手机号')
driver.find_element(*loc_click_choose).click()  # 点击选择收货地址
print('点击选择收货地址')
driver.find_element(*loc_keyword).send_keys(keyword)  # 输入关键字
time.sleep(5)
print('输入关键字')
driver.find_element(*loc_choose).click()  # 选择地址
print('选择地址')
driver.find_element(*loc_doorplate).send_keys(doorplate)  # 输入楼号门牌
print('输入楼号门牌')
driver.find_element(*loc_tag).click()  # 标签选择公司
print('标签选择公司')
driver.find_element(*loc_default_address).click()  # 设置默认地址
print('设置默认地址')
driver.find_element(*loc_save).click()  # 保存收货地址
time.sleep(1)
print('保存收货地址')
text = driver.find_element(*loc_assert).text  # 获取断言
print('获取断言')
unittest.TestCase().assertEqual('香山艺墅701', text)  # 断言

driver.quit()
print('退出')