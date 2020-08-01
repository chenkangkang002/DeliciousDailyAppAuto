'''购物车页面类'''
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ShoppingCartPage(BasePage):
    '''购物车页面类'''

    #定位器
    locator_shoppingcart = (By.ID,'cn.missfresh.application:id/cartTab')
    locator_shoppingcart_page = (By.ID, 'cn.missfresh.application:id/rcv_product')
    locator_go_shopping = (By.ID,'cn.missfresh.application:id/tv_go')
    locator_back_shoppingcart_from_view = (By.ID, 'cn.missfresh.application:id/img_back')
    locator_ele_select_all = (By.ID, 'cn.missfresh.application:id/cb_select_all')
    locator_delete_button = (By.ID, 'cn.missfresh.application:id/tv_delete')
    locator_ensure_delete = (By.ID, 'cn.missfresh.application:id/tv_ensure')
    locator_go_to_pay = (By.ID,'cn.missfresh.application:id/tv_checkout')
    addr_path = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    locator_get_in_address = (By.XPATH, addr_path)
    locator_addr_list = (By.ID, 'cn.missfresh.application:id/lv_address')
    locator_select_pay_way = (By.ID, 'cn.missfresh.application:id/confirm_recycler_view')
    locator_pay_button = (By.ID, 'cn.missfresh.application:id/tv_confirm')
    locator_add_addr = (By.ID,'cn.missfresh.application:id/btn_add_address')

    def get_in_shoppingcart(self):
        '''进入购物车'''
        self.driver.find_element(*self.locator_shoppingcart).click()

    def go_shopping(self):
        '''点击【去逛逛】进入首页'''
        #仅限购物车为空时使用
        self.driver.find_element(*self.locator_go_shopping).click()

    def add_recommend_product(self,product_index=1):
        '''
        添加推荐商品
        product_index:商品顺序,数据为int型,默认为1
        '''
        locator = self.driver.find_element(*self.locator_shoppingcart_page)
        judge_path = '//android.widget.RelativeLayout[' + str(product_index) + ']/android.widget.ImageView[3]'
        judge = locator.find_element(By.XPATH,judge_path).get_attribute('resourceId')
        if judge == 'cn.missfresh.application:id/btn_main_item_buy_now':
            path = '//android.widget.RelativeLayout[' + str(product_index) + ']/android.widget.ImageView[3]'
            locator.find_element(By.XPATH,path).click()
            self.swipe_to('down')
            time.sleep(1)
        else:
            path = '//android.widget.RelativeLayout[' + str(product_index) + ']/android.widget.ImageView[4]'
            locator.find_element(By.XPATH, path).click()
            self.swipe_to('down')
            time.sleep(1)

    def edit_product_num(self,product_index=1,action='add'):
        '''
        编辑商品数量
        product_index：商品顺序,数据为int型,默认为1
        action：增加或减少商品数量，增加为add，减少为sub，默认为add
        '''
        #//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[5]
        #//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[5]
        #//android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]
        locator = self.driver.find_element(*self.locator_shoppingcart_page)
        index = product_index+1
        if action == 'add':
            path = '//android.widget.LinearLayout[' + str(index) + ']/android.widget.RelativeLayout[1]/android.widget.ImageView[5]'
            locator.find_element(By.XPATH, path).click()
        elif action == 'sub':
            path = '//android.widget.LinearLayout[' + str(index) + ']/android.widget.RelativeLayout[1]/android.widget.ImageView[4]'
            locator.find_element(By.XPATH,path).click()

    def view_product(self,product_index=1):
        '''
        查看商品详情
        product_index：商品顺序,数据为int型,默认为1
        '''
        index = product_index+1
        locator = self.driver.find_element(*self.locator_shoppingcart_page)
        path = '//android.widget.LinearLayout[' + str(index) + ']/android.widget.RelativeLayout[1]/android.widget.ImageView[2]'
        locator.find_element(By.XPATH, path).click()

    def back_shoppingcart_from_view(self):
        '''从商品详情页返回购物车'''
        self.driver.find_element(*self.locator_back_shoppingcart_from_view).click()

    def ele_select_all(self):
        '''点击全选'''
        self.driver.find_element(*self.locator_ele_select_all).click()

    def select_product(self,product_index=1):
        '''
        选择商品
        product_index：商品顺序,数据为int型,默认为1
        '''
        index = product_index+1
        locator = self.driver.find_element(*self.locator_shoppingcart_page)
        path = '//android.widget.LinearLayout[' + str(index) + ']/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
        locator.find_element(By.XPATH, path).click()

    def delete_button(self):
        '''删除按钮'''
        self.driver.find_element(*self.locator_delete_button).click()
        time.sleep(1)

    def ensure_delete(self):
        '''确认删除'''
        self.driver.find_element(*self.locator_ensure_delete).click()

    def go_to_pay(self):
        '''去结算页面'''
        self.driver.find_element(*self.locator_go_to_pay).click()

    def get_in_address(self):
        '''去收货地址页面'''
        self.driver.find_element(*self.locator_get_in_address).click()

    def select_address(self,addr_index=1):
        '''
        选择收货地址
        index:收货地址顺序，默认为1（第一个）
        '''
        loc = self.driver.find_element(*self.locator_addr_list)
        path = '//android.widget.LinearLayout[' + str(addr_index) + ']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]'
        loc.find_element(By.XPATH,path).click()

    def edit_address(self,index=1,action='add'):
        '''
        新增或修改收货地址
        index:收货地址顺序，默认为1（第一个）#index只对修改地址有效
        action：新增(add)或修改(modify)收货地址，默认为add
        '''
        if action == 'add':
            self.driver.find_element(*self.locator_add_addr).click()
        elif action == 'modify':
            #//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]
            loc = self.driver.find_element(*self.locator_addr_list)
            path = '//android.widget.LinearLayout[' + str(index) + ']/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]'
            loc.find_element(By.XPATH,path).click()

    def select_pay_way(self,pay_index=5):
        '''
        选择支付方式
        index:支付方式，5为微信，6为支付宝，7为花呗,默认为微信支付5
        '''
        loc = self.driver.find_element(*self.locator_select_pay_way)
        path = '//android.widget.RelativeLayout[' + str(pay_index) + ']/android.widget.ImageView[2]'
        loc.find_element(By.XPATH,path).click()

    def pay_button(self):
        '''点击支付按钮'''
        self.driver.find_element(*self.locator_pay_button).click()

    def shopping_cart_flow(self,addr_index=1,pay_index=5):
        '''购物车购物流程'''
        #适用于已向购物车添加商品的情况
        self.get_in_shoppingcart()
        self.swipe_to('down')
        self.go_to_pay()
        self.get_in_address()
        self.select_address(addr_index)
        self.select_pay_way(pay_index)
        self.pay_button()

    def modify_product_num_flow(self,product_index=1,action='add'):
        '''进入修改购物车商品数量'''
        #适用于购物车中已有商品的情况
        self.get_in_shoppingcart()
        self.swipe_to('down')
        time.sleep(2)
        self.edit_product_num(product_index,action)
