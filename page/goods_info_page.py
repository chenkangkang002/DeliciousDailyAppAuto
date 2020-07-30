'''
商品详情page
'''
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class GoodsInfoPage(BasePage):

    '''定位符'''
    loc_goods_info_back = (By.ID, 'cn.missfresh.application:id/img_back')   #返回上一页
    loc_goods_info_share = (By.ID, 'cn.missfresh.application:id/img_share')   #分享
    loc_goods_info_cart_view = (By.ID, 'cn.missfresh.application:id/iv_cart_icon')    #查看购物车
    loc_goods_info_add_cart = (By.XPATH, '//android.widget.TextView[@text=\"加入购物车\"]')     #加入购物车
    loc_goods_info_now_pay = (By.XPATH, '//android.widget.TextView[@text=\"立即购买\"]')     #立即购买
    loc_goods_info_title = (By.ID, 'cn.missfresh.application:id/ll_title')   #顶部导航栏
    loc_goods_info_title_class = (By.CLASS_NAME, 'android.widget.TextView')   #顶部title控件集合
    loc_goods_inf0_share_cancle = (By.ID, 'cn.missfresh.application:id/btn_share_cancle')   #取消分享
    loc_share_wechat_session = (By.ID, 'cn.missfresh.application:id/btn_share_wechat_session')   #通过微信分享
    loc_share_wechat_timeline = (By.ID, 'cn.missfresh.application:id/btn_share_wechat_timeline')    #分享朋友圈

    '''控件单方法实现'''
    def click_share_wechat_timeline(self):
        '''点击朋友圈分享'''
        self.find_element(self.loc_share_wechat_timeline).click()

    def click_share_wechat_session(self):
        '''点击微信分享'''
        self.find_element(self.loc_share_wechat_session).click()

    def click_goods_inf0_share_cancle(self):
        '''点击取消分享'''
        self.find_element(self.loc_goods_inf0_share_cancle).click()

    def click_goods_info_title_class(self):
        '''随机点击顶部导航栏的商品、推荐、详情，下拉之后才出现'''
        ele = self.get_element_random(self.loc_goods_info_title,
                                self.loc_goods_info_title_class)
        ele.click()

    def click_goods_info_now_pay(self):
        '''点击立即购买'''
        self.find_element(self.loc_goods_info_now_pay).click()

    def click_goods_info_add_cart(self):
        '''点击加入购物车'''
        self.find_element(self.loc_goods_info_add_cart).click()

    def click_goods_info_cart_view(self):
        '''点击购物车，查看购物车信息'''
        self.find_element(self.loc_goods_info_cart_view).click()

    def click_goods_info_share(self):
        '''点击分享'''
        self.find_element(self.loc_goods_info_share).click()

    def click_goods_info_back(self):
        '''点击返回上一页<'''
        self.find_element(self.loc_goods_info_back).click()

    '''界面功能实现'''
