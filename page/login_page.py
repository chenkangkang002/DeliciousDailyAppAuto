'''登录'''
from page.base_page import BasePage

class LoginPage(BasePage):
    '''控件定位'''
    loc_my = 'cn.missfresh.application:id/mineTab'  # 我的
    loc_login_sign = 'cn.missfresh.application:id/tv_nickname'  # 登录
    loc_phone = 'cn.missfresh.application:id/phoneNumber_et'  # 手机号
    loc_get_check_code = 'cn.missfresh.application:id/getCheckCode'  #获取验证码按钮
    loc_check_code = 'cn.missfresh.application:id/checkCode_et'  # 验证码
    loc_deal = 'cn.missfresh.application:id/iv_protocol'  # 勾选协议
    loc_click_login = 'cn.missfresh.application:id/btn_login'  #登录按钮
    loc_assert = 'cn.missfresh.application:id/tv_nickname'  # 断言

    def click_me(self):
        '''点击我的'''
        self.driver.find_element_by_id(self.loc_my).click()
        print('点击我的')

    def login_sign(self):
        '''点击登录/注册'''
        self.driver.find_element_by_id(self.loc_login_sign).click()
        print('点击登录/注册')

    def phone(self,phone):
        '''输入手机号'''
        self.driver.find_element_by_id(self.loc_phone).send_keys(phone)
        print('输入手机号')

    def get_check_code(self):
        '''点击获取验证码'''
        self.driver.find_element_by_id(self.loc_get_check_code).click()
        print('点击获取验证码')

    def check_code(self):
        '''输入验证码'''
        check_code = input('请输入验证码：')
        self.driver.find_element_by_id(self.loc_check_code).send_keys(check_code)
        print('\n输入验证码')

    def deal(self):
        '''勾选协议'''
        self.driver.find_element_by_id(self.loc_deal).click()
        print('勾选协议')

    def click_login(self):
        '''点击登录'''
        self.driver.find_element_by_id(self.loc_click_login).click()
        print('点击登录')

    def login(self,phone):
        '''登录逻辑'''
        self.click_me()
        self.login_sign()
        self.phone(phone)
        self.get_check_code()
        self.check_code()
        self.deal()
        self.click_login()
        text = self.assert_text(self.loc_assert)
        return text