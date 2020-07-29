'''登录用例'''
from page.login_page import LoginPage
from testcase.base_test import BaseTestCase


class LoginTestCase(BaseTestCase):
    def test_login(self):
        login = LoginPage(self.driver)
        phone = '18380251182'
        text = login.login(phone)
        self.assertEqual('小鲜',text)