'''
示例
'''
from selenium.webdriver.common.by import By

from activity.base_activity import BaseActivity


class ExamplesActivity(BaseActivity):

    '''定位符'''
    loc_login_name = (By.ID, 'u_name')   #登录用户名
    loc_login_password = (By.ID, 'password')    #登录用户密码
    loc_login_submit = (By.ID, 'login_submit')  #登录按钮

    '''初始化：根据自己的情况进行定义'''
    def __init__(self):
        pass

    '''控件的单个功能实现'''
    def input_login_name(self, u_name):
        '''
        输入登录用户名
        :param u_name: 登录用户用户名
        :return:
        '''
        self.find_element(self.loc_login_name).clear()
        self.find_element(self.loc_login_name).click(u_name)

    def input_login_password(self, password):
        '''
        输入登录用户的密码
        :param password: 登录用户的密码
        :return:
        '''
        self.find_element(self.loc_login_password).clear()
        self.find_element(self.loc_login_password).click(password)

    def click_login_submit(self):
        '''点击登录按钮'''
        self.find_element(self.loc_login_submit).click()

    '''页面功能实现'''
    def login(self, u_name, u_password):
        '''实现登录功能'''
        self.input_login_name(u_name)
        self.input_login_password(u_password)
        self.click_login_submit()
