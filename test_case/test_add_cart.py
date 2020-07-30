'''
各种方式的添加商品到购物车
'''
from page.classify_page import ClassifyPage
from page.goods_info_page import GoodsInfoPage
from page.home_page import HomePage
from page.search_page import SearchPage
from test_case.base_test import BaseTestCase


class AddCartTestCase(BaseTestCase):

    def test_add_cart_random(self):
        '''在分类主页随机添加商品到购物车'''
        #实例化首页page
        hp = HomePage(self.driver)
        hp.ele_classification()
        #实例化分类page
        cp = ClassifyPage(self.driver)
        cp.click_top_navigations()
        cp.click_left_navigations()
        cp.click_goods_add_cart()

    def test_search_add_cart_random(self):
        '''在分类主页先搜索，在搜索结果中随机添加商品到购物车'''
        # 实例化首页page
        hp = HomePage(self.driver)
        hp.ele_classification()
        #实例化搜索page
        sp = SearchPage(self.driver)
        context = '芒果'
        sp.search_goods(context)    #搜索商品
        sp.click_search_result_add_cart()   #随机添加搜索结果到购物车

    def test_goods_info_add_cart_random(self):
        '''随机选择商品进入商品详情页加入商品到购物车'''
        # 实例化首页page
        hp = HomePage(self.driver)
        hp.ele_classification()
        #初始化分类page
        cp = ClassifyPage(self.driver)
        cp.random_choose_goods()
        #初始化商品详情page
        gip = GoodsInfoPage(self.driver)
        gip.click_goods_info_add_cart()