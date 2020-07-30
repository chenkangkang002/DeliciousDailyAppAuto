from driver import driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.unlock_page import unlock
from test_case.base_test import BaseTestCase


class HomeBuyCase(BaseTestCase):
    def test_room_buy(self):
        '''浏览商品并立即购买'''
        passwd = [0, 1, 2, 5, 4, 3, 6, 7, 8]  # 确定密码的排列顺序
        unlock(passwd)  # 解锁
        p = HomePage(driver)
        mf_goods = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.View/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView[1]'
        p.buy(mf_goods)
        h = LoginPage(self.driver)  # 登录
        phone = "18188391365"  # 输入电话号码
        h.mlogin(phone)
        # 点击请选择收获地址
        # 新增收货地址
        # 点击去结算

