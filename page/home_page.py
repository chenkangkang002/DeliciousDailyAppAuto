from selenium.webdriver.common.by import By

from driver.driver import get_driver
from test_case.base_test import BaseTestCase

class HomePage():
    '''首页'''
    mf_select = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.TextView')
    mf_input = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                         '.FrameLayout/android.view.View/android.widget.EditText')
    mf_button = (By.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                 '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                 '.View/android.widget.TextView')
    mf_na = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
             '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
             '.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget'
             '.RecyclerView/android.widget.TextView[5]')
    mf_add = (By.XPATH,
              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
              '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android'
              '.widget.FrameLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.widget'
              '.RelativeLayout[3]/android.widget.FrameLayout[2]/android.widget.RelativeLayout['
              '2]/android.widget.FrameLayout/android.widget.TextView')
    mf_in = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
             '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android'
             '.widget.ImageView[3]')
    mf_start = (By.XPATH,
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                '.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview'
                '.widget.RecyclerView/android.widget.TextView[1]')
    mf_end = (By.XPATH,
              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
              '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
              '.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget'
              '.RecyclerView/android.widget.TextView[5]')
    mf_classification = (By.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                         '.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView')
    mf_ShoppingCart = (By.XPATH,
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView[1]')
    mf_user = (By.XPATH,
             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.TextView')
    mf_buy = (By.XPATH,
              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]')
    def __init__(self,driver):
        self.driver = driver

    def ele_swipe(self, sx, sy, ex, ey):
        '''屏幕滑动'''
        self.driver.swipe(sx, sy, ex, ey, 300)

    def ele_na(self):
        '''点击导航栏肉蛋食材'''
        self.driver.find_element(*self.mf_na).click()

    def ele_select(self):
        '''点击搜索框'''
        self.driver.find_element(*self.mf_select).click()  # 点击搜索框

    def ele_input(self, trade_name):
        '''输入内容'''
        self.driver.find_element(*self.mf_input).clear()  # 点击清空输入框
        self.driver.find_element(*self.mf_input).send_keys(trade_name)  # 输入内容

    def ele_button(self):
        '''点击搜索按钮'''
        self.driver.find_element(*self.mf_button).click()  # 点击搜索按钮

    def ele_scroll(self):
        '''页面滚动'''
        start_ele = self.driver.find_element(*self.mf_start)
        end_ele = self.driver.find_element(*self.mf_end)
        self.driver.scroll(start_ele, end_ele)

    def ele_goods(self, mf_goods):
        '''点击商品'''
        self.driver.find_element(By.XPATH, mf_goods).click()

    def ele_buy(self):
        '''点击立即购买'''
        self.driver.find_element(*self.mf_buy).click()

    def ele_add(self):
        '''点击加入购物车'''
        self.driver.find_element(*self.mf_add).click()

    def ele_in(self):
        '''点击进入购物车'''
        self.driver.find_element(*self.mf_in).click()

    def ele_classification(self):
        '''进入分类'''
        self.driver.find_element(*self.mf_classification)

    def ele_ShoppingCart(self):
        '''进入购物车'''
        self.driver.find_element(*self.mf_ShoppingCart)

    def ele_user(self):
        '''进入我的'''
        self.driver.find_element(*self.mf_user)

    def buy(self, mf_goods):
        '''浏览商品立即购买'''
        self.ele_scroll()  # 右滑到肉蛋食材
        self.ele_na()  # 点击肉蛋食材
        self.ele_goods(mf_goods)  # 点击德清源谷物鸡蛋
        self.ele_buy()  # 点击立即购买
        # 登录
        # 点击请选择收获地址
        # 新增收货地址
        # 点击去结算
        # 登录

    def select(self, trade_name):
        '''搜索'''
        self.ele_select()  # 点击搜索框
        self.ele_input(trade_name)  # 清空并输入内容
        self.ele_button()  # 点击搜索
        self.ele_add()  # 点击加入购物车图标
        self.ele_in()  # 点击进入购物车
        # 点击去结算
        # 登录


# p = HomePage(driver)
# mf_goods = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.View/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView[1]'
#
# p.buy(mf_goods)

# p = HomePage(driver)
# p.select('螺蛳粉')











