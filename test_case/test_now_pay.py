'''
购买商品
'''
from page.classify_page import ClassifyPage
from page.goods_info_page import GoodsInfoPage
from page.home_page import HomePage
from test_case.base_test import BaseTestCase


class NowPayTestCase(BaseTestCase):

    def test_now_pay(self):
        '''从分类页面进入，随机选择商品，购买商品'''
        # 实例化首页page
        hp = HomePage(self.driver)
        hp.ele_classification()
        #实例化分类page
        cp = ClassifyPage(self.driver)
        cp.click_top_navigations()  #随机选择top类
        cp.click_left_navigations() #随机选择left分类
        cp.click_goods_navigations()    #随机选择商品
        #实例化商品详情page
        gip = GoodsInfoPage(self.driver)
        gip.click_goods_info_now_pay()  #点击立即购买