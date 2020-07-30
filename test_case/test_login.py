'''登录用例'''
from page.login_page import LoginPage
from test_case.base_test import BaseTestCase

class LoginTestCase(BaseTestCase):
    def test_login(self):
        login = LoginPage(self.driver)  # 实例化LoginPage
        login.click_me()  # 调用LoginPage的click_me()方法
        login.login_sign()  # 调用LoginPage的login_sign()方法
        phone = '18380251182'
        text = login.mlogin(phone)  # 调用LoginPage的mlogin()方法
        self.assertEqual('小鲜', text)  # 进行断言