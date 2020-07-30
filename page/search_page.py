'''
商品专属搜索page
'''
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class SearchPage(BasePage):

    '''定位符'''
    loc_search_box = (By.ID, 'cn.missfresh.application:id/search_view')     #搜索框
    loc_search_button = (By.ID, 'cn.missfresh.application:id/tv_search')  #搜索按钮
    loc_clear_history = (By.ID, 'cn.missfresh.application:id/clear_his_view')   #清空历史记录按钮
    loc_history_search_list = (By.ID, 'cn.missfresh.application:id/history_layout')    #历史搜索列表父级
    loc_history_search_class = (By.CLASS_NAME, 'android.widget.TextView')   #历史搜索里的结果
    loc_hot_search_list = (By.ID, 'cn.missfresh.application:id/hot_layout')     #热门搜索列表父级
    loc_hot_search_class = (By.CLASS_NAME, 'android.widget.TextView')    #热门搜索里面的结果
    loc_cancel_tv = (By.ID, 'cn.missfresh.application:id/cancel_tv')    #清空搜索历史信息弹框取消按钮
    loc_submit_tv = (By.ID, 'cn.missfresh.application:id/submit_tv')  #清空搜索历史信息弹框确认按钮
    loc_search_back_view = (By.ID, 'cn.missfresh.application:id/search_back_view')   #返回按钮<
    #搜索结果
    loc_cart_view = (By.ID, 'cn.missfresh.application:id/cart_view')  # 搜索结果页面购物车
    loc_search_result_recycler = (By.ID, 'cn.missfresh.application:id/result_recycler')   #搜索结果商品展示框
    loc_search_result_class = (By.CLASS_NAME, 'android.widget.RelativeLayout')   #搜索结果对象集合
    loc_search_result_add_cart = (By.ID, 'cn.missfresh.application:id/btn_main_item_buy_now')    #搜索结果添加到购物车

    '''控件单个功能'''
    def click_search_result_add_cart(self):
        '''随机添加搜索结果中的某商品到购物车'''
        ele = self.get_element_random(self.loc_search_result_recycler,
                                      self.loc_search_result_class,
                                      self.loc_search_result_add_cart)
        ele.click()

    def click_search_result_class(self):
        '''随机点击搜索结果中的某个商品'''
        ele = self.get_element_random(self.loc_search_result_recycler,
                                self.loc_search_result_class)
        ele.click()
    def click_cart_view(self):
        '''点击搜索结果界面的购物车图标'''
        self.find_element(self.loc_cart_view).click()

    def click_search_back_view(self):
        '''点击返回上一个页面'''
        self.find_element(self.loc_search_back_view).click()

    def click_clear_history(self):
        '''点击历史搜索信息清空按钮'''
        self.find_element(self.loc_clear_history).click()

    def input_search_box(self, context):
        '''搜索框输入信息'''
        self.find_element(self.loc_search_box).clear()
        self.find_element(self.loc_search_box).send_keys(context)

    def click_search_button(self):
        '''点击搜索按钮'''
        self.find_element(self.loc_search_button).click()

    def click_history_search_class(self):
        '''随机点击历史搜索内的内容'''
        ele = self.get_element_random(self.loc_history_search_list,
                                        self.loc_history_search_class)
        ele.click()

    def click_hot_search_class(self):
        '''随机点击热门搜索内的内容'''
        ele = self.get_element_random(self.loc_hot_search_list,
                                        self.loc_hot_search_class)
        ele.click()

    def click_cancel_tv(self):
        '''点击弹框取消'''
        self.find_element(self.loc_cancel_tv).click()

    def click_submit_tv(self):
        '''点击弹框确定按钮'''
        self.find_element(self.loc_submit_tv).click()

    '''页面功能'''
    def search_goods(self, context):
        '''在搜索商品页面搜索商品'''
        self.input_search_box(context)
        self.click_search_button()
