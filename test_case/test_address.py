'''新增收货地址用例'''
from page.address_page import AddAddressPage
from page.login_page import LoginPage
from test_case.base_test import BaseTestCase


class AddAddressTestCase(BaseTestCase):
    def test_add_address(self):
        login = LoginPage(self.driver)  # 实例化LoginPage
        login.click_me()  # 调用LoginPage的click_me()方法
        login.login_sign()  # 调用LoginPage的login_sign()方法
        phone = '18380251182'
        text = login.mlogin(phone)  # 调用LoginPage的mlogin()方法
        self.assertEqual('小鲜', text)  # 进行断言

        address = AddAddressPage(self.driver)  # 实例化AddAddressPage
        receiver = '李白'
        tel = '18380251182'
        keyword = '香山'
        doorplate = '701'
        text = address.address(receiver, tel, keyword, doorplate)  # 调用AddAddressPage的address()方法
        self.assertEqual('香山艺墅701', text)  # 断言