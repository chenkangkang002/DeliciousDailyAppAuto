'''
分类主页page
'''
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ClassifyPage(BasePage):

    '''定位器'''
    loc_classify_top = (By.ID, 'cn.missfresh.application:id/rv_top_label')  #顶部导航
    loc_classify_top_navigations = (By.CLASS_NAME, 'android.widget.LinearLayout')  #顶部导航栏控件集合
    loc_classify_left = (By.ID, 'cn.missfresh.application:id/rlv_classify') #左边导航栏
    loc_classify_left_navigations = (By.CLASS_NAME, 'android.widget.FrameLayout')   #左边导航栏控件集合
    loc_classify_goods = (By.ID, 'cn.missfresh.application:id/recycler_view')   #商品列表
    loc_classify_goods_list = (By.CLASS_NAME, 'android.widget.RelativeLayout')  #商品列表控件集合
    loc_classify_add_cart = (By.ID, 'cn.missfresh.application:id/btn_main_item_buy_now')    #添加购物车+
    loc_tv_main_item_sub = (By.ID, 'cn.missfresh.application:id/tv_main_item_sub')   #减少商品数量按钮-
    loc_sort_sales_volume = (By.ID, 'cn.missfresh.application:id/tv_sales_count')   #排序销量按钮
    loc_sort_multiple = (By.ID, 'cn.missfresh.application:id/tv_synthesize')     #排序综合按钮
    loc_sort_price = (By.ID, 'cn.missfresh.application:id/price_layout')     #排序价格按钮

    '''控件单功能'''
    def click_tv_main_item_sub(self):
        '''点击减少商品数量按钮，存在添加商品在购物车时出现'''
        self.find_element(self.loc_tv_main_item_sub).click()

    def click_sort_price(self):
        '''点击价格，进行排序'''
        self.find_element(self.loc_sort_price).click()

    def click_sort_multiple(self):
        '''点击销量，进行排序'''
        self.find_element(self.loc_sort_multiple).click()

    def click_sort_sales_volume(self):
        '''点击销量，进行排序'''
        self.find_element(self.loc_sort_sales_volume).click()

    def click_top_navigations(self):
        '''点击—顶部导航某单元'''
        #获得列表中的某个控件
        ele = self.get_element_random(self.loc_classify_top,
                                      self.loc_classify_top_navigations)
        ele.click()

    def click_left_navigations(self):
        '''点击—左边导航某单元'''
        # 获得列表中的某个控件
        ele = self.get_element_random(self.loc_classify_left,
                                      self.loc_classify_left_navigations)
        ele.click()

    def click_goods_navigations(self):
        '''点击—商品列表某单元'''
        # 获得列表中的某个控件
        ele = self.get_element_random(self.loc_classify_goods,
                                      self.loc_classify_goods_list)
        ele.click()

    def click_goods_add_cart(self):
        '''点击—添加商品到购物车'''
        # 获得列表中的某个控件
        ele = self.get_element_random(self.loc_classify_goods,
                                      self.loc_classify_goods_list,
                                      self.loc_classify_add_cart)
        ele.click()

    '''界面实现功能'''