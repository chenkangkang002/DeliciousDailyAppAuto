'''新增收货地址'''
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class AddAddressPage(BasePage):
    '''控件定位'''
    loc_click_address = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]')  # 【收货地址】定位
    loc_click_add_address = (By.ID,'cn.missfresh.application:id/btn_add_address')  # 【新增收货地址】定位
    loc_receiver = (By.ID,'cn.missfresh.application:id/et_edit_address_receiver')  # 收货人定位
    loc_sir = (By.ID,'cn.missfresh.application:id/rg_sex_sir')  # 先生
    loc_tel = (By.ID,'cn.missfresh.application:id/et_edit_address_tel')  # 手机号码
    loc_click_choose = (By.ID,'cn.missfresh.application:id/tv_edit_detail_address')  # 收货地址输入框
    loc_keyword = (By.ID,'cn.missfresh.application:id/et_search_address_input')  # 关键字
    loc_choose = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout')  # 选择地址
    loc_doorplate = (By.ID,'cn.missfresh.application:id/et_edit_doorplate')  # 楼号门牌
    loc_tag = (By.ID,'cn.missfresh.application:id/rb_company_address_tags')  # 公司标签
    loc_default_address = (By.ID,'cn.missfresh.application:id/ssb_default_address_switch')  # 设置默认地址
    loc_save = (By.ID,'cn.missfresh.application:id/btn_save_address')  # 保存收获地址
    loc_assert = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]')  # 断言

    def click_address(self):
        '''点击收货地址'''
        self.find_element(self.loc_click_address).click()
        time.sleep(1)
        print('点击收货地址')

    def click_add_address(self):
        '''点击新增收货地址'''
        self.find_element(self.loc_click_add_address).click()
        time.sleep(1)
        print('点击新增收货地址')

    def receiver(self,receiver):
        '''输入收货人'''
        self.find_element(self.loc_receiver).clear()  # 清空收货人
        self.find_element(self.loc_receiver).send_keys(receiver)  # 输入收货人
        time.sleep(1)
        print('输入收货人')

    def sir(self):
        '''性别选择先生'''
        self.find_element(self.loc_sir).click()
        time.sleep(1)
        print('性别选择先生')

    def tel(self,tel):
        '''输入手机号'''
        self.find_element(self.loc_tel).clear()  # 清空手机号
        self.find_element(self.loc_tel).send_keys(tel)  # 输入手机号
        time.sleep(1)
        print('输入手机号')

    def click_choose(self):
        '''点击选择收货地址'''
        self.find_element(self.loc_click_choose).click()
        time.sleep(1)
        print('点击选择收货地址')

    def keyword(self,keyword):
        '''输入关键字'''
        self.find_element(self.loc_keyword).send_keys(keyword)
        time.sleep(5)
        print('输入关键字')

    def choose(self):
        '''选择地址'''
        self.find_element(self.loc_choose).click()
        time.sleep(1)
        print('选择地址')

    def doorplate(self,doorplate):
        '''输入楼号门牌'''
        self.find_element(self.loc_doorplate).send_keys(doorplate)
        time.sleep(1)
        print('输入楼号门牌')

    def tag(self):
        '''标签选择公司'''
        self.find_element(self.loc_tag).click()
        time.sleep(1)
        print('标签选择公司')

    def default_address(self):
        '''设置默认地址'''
        self.find_element(self.loc_default_address).click()
        time.sleep(1)
        print('设置默认地址')

    def save(self):
        '''保存收货地址'''
        self.find_element(self.loc_save).click()
        time.sleep(1)
        print('保存收货地址')

    def address(self,receiver,tel,keyword,doorplate):
        self.click_address()
        self.click_add_address()
        self.receiver(receiver)
        self.sir()
        self.tel(tel)
        self.click_choose()
        self.keyword(keyword)
        self.choose()
        self.doorplate(doorplate)
        self.tag()
        self.default_address()
        self.save()
        text = self.assert_text(self.loc_assert)
        time.sleep(1)
        self.screenshot('address')  # 截图
        time.sleep(1)
        return text