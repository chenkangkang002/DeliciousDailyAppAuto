
from page.home_page import HomePage
from page.login_page import LoginPage
from page.unlock_page import unlock
from test_case.base_test import BaseTestCase


class HomeSelectCase(BaseTestCase):
    def test_room_select(self):
        '''搜索'''
        passwd = [0, 1, 2, 5, 4, 3, 6, 7, 8]  # 确定密码的排列顺序
        unlock(passwd)     #解锁
        p = HomePage(self.driver)   #实例化HomePage类
        p.select('螺蛳粉')      #搜索螺蛳粉并理解购买
        #点击去结算
        h = LoginPage(self.driver)     #登录
        phone = "18188391365"        #输入电话号码
        h.mlogin(phone)