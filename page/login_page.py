'''登录'''
import time

from selenium.webdriver.common.by import By
from page.base_page import BasePage

class LoginPage(BasePage):
    '''控件定位'''
    loc_my = (By.ID,'cn.missfresh.application:id/mineTab')  # 我的
    loc_login_sign = (By.ID,'cn.missfresh.application:id/tv_nickname')  # 登录
    loc_phone = (By.ID,'cn.missfresh.application:id/phoneNumber_et')  # 手机号
    loc_get_check_code = (By.ID,'cn.missfresh.application:id/getCheckCode')  #获取验证码按钮
    loc_check_code = (By.ID,'cn.missfresh.application:id/checkCode_et')  # 验证码
    loc_deal = (By.ID,'cn.missfresh.application:id/iv_protocol')  # 勾选协议
    loc_click_login = (By.ID,'cn.missfresh.application:id/btn_login')  #登录按钮
    loc_assert = (By.ID,'cn.missfresh.application:id/tv_nickname')  # 断言

    def click_me(self):
        '''点击我的'''
        self.find_element(self.loc_my).click()
        time.sleep(1)
        print('点击我的')

    def login_sign(self):
        '''点击登录/注册'''
        self.find_element(self.loc_login_sign).click()
        time.sleep(1)
        print('点击登录/注册')

    def phone(self,phone):
        '''输入手机号'''
        self.find_element(self.loc_phone).send_keys(phone)
        time.sleep(1)
        print('输入手机号')

    def get_check_code(self):
        '''点击获取验证码'''
        self.find_element(self.loc_get_check_code).click()
        time.sleep(1)
        print('点击获取验证码')

    def check_code(self):
        '''输入验证码'''
        check_code = input('请输入验证码：')
        self.find_element(self.loc_check_code).send_keys(check_code)
        time.sleep(1)
        print('\n输入验证码')

    def deal(self):
        '''勾选协议'''
        self.find_element(self.loc_deal).click()
        time.sleep(3)
        print('勾选协议')

    def click_login(self):
        '''点击登录'''
        self.find_element(self.loc_click_login).click()
        time.sleep(1)
        print('点击登录')

    def mlogin(self,phone):
        '''中途登录'''
        self.phone(phone)  # 输入手机号
        self.get_check_code()  # 点击【获取验证码】
        self.check_code()  # 输入验证码
        self.deal()  # 勾选协议
        self.click_login()  # 点击【登录】
        text = self.assert_text(self.loc_assert)  # 获取断言
        time.sleep(1)
        self.screenshot('login')  # 截图
        time.sleep(1)
        return text