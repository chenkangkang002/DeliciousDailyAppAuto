'''购物车线性脚本'''
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from line_script.method import swipe_to


#初始化驱动
desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:62001',
    'platformVersion':'5.1.1',
    'appPackage':'cn.missfresh.application',
    'appActivity':'cn.missfresh.module.base.main.view.SplashActivity',
    'noReset': True,  # 开启APP不重置
    'unicodeKeyboard': True,  # 打开unicode输入法，能够输入中文
    'resetKeyboard': True  # 还原输入法
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
driver.implicitly_wait(30)
time.sleep(3)
#进入购物车
driver.find_element(By.ID,'cn.missfresh.application:id/cartTab').click()
time.sleep(1)
#向下滑动刷新
swipe_to(driver,'down')
time.sleep(1)
#点击去逛逛进入首页浏览商品
driver.find_element(By.ID,'cn.missfresh.application:id/tv_go').click()
time.sleep(1)
swipe_to(driver)
time.sleep(1)
#回到购物车
driver.find_element(By.ID,'cn.missfresh.application:id/cartTab').click()
time.sleep(1)
#在购物车内添加商品
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.RelativeLayout[2]/android.widget.ImageView[3]
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[3]
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[3]
# path1 = '//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/rcv_product"]/android.widget.RelativeLayout[2]/android.widget.ImageView[3]'
# path2 = '//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/rcv_product"]/android.widget.RelativeLayout[1]/android.widget.ImageView[3]'
# driver.find_element(By.XPATH,path1).click()
# #下拉刷新
# swipe_to(driver,'down')
# time.sleep(1)
# driver.find_element(By.XPATH,path2).click()
path1 = '//android.widget.RelativeLayout[1]/android.widget.ImageView[3]'
path2 = '//android.widget.RelativeLayout[2]/android.widget.ImageView[4]'
locator = driver.find_element(By.ID,'cn.missfresh.application:id/rcv_product')
locator.find_element(By.XPATH,path1).click()
#下拉刷新
swipe_to(driver,'down')
time.sleep(1)
locator.find_element(By.XPATH,path2).click()
#下拉刷新
swipe_to(driver,'down')
time.sleep(1)
#查看购物车商品详情
#//android.widget.RelativeLayout[@resource-id=\"cn.missfresh.application:id/ll_buy_product_bg\"]/android.widget.ImageView[2]
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]
#//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]
path = '//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]'
locator = driver.find_element(By.ID,'cn.missfresh.application:id/rcv_product')
locator.find_element(By.XPATH,path).click()
time.sleep(1)
#上划浏览
swipe_to(driver)
time.sleep(1)
#从详情页返回购物车
driver.find_element(By.ID,'cn.missfresh.application:id/img_back').click()
time.sleep(1)
#增加商品数量
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[5]
add_path = '//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[5]'
locator.find_element(By.XPATH,add_path).click()
time.sleep(1)
#减少商品数量
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[4]
delt_path = '//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[4]'
locator.find_element(By.XPATH,delt_path).click()
time.sleep(1)
#选择与取消全选商品
driver.find_element(By.ID,'cn.missfresh.application:id/cb_select_all').click()
time.sleep(1)
#选择单个商品
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]
sel_path = '//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
locator.find_element(By.XPATH,sel_path).click()
time.sleep(1)
#点击去结算
driver.find_element(By.ID,'cn.missfresh.application:id/tv_checkout').click()
time.sleep(1)
#选择收货地址
#//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]
#//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]
ab_path = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
driver.find_element(By.XPATH,ab_path).click()
time.sleep(1)
#//android.widget.ListView[@resource-id=\"cn.missfresh.application:id/lv_address\"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]
#//android.widget.ListView[@resource-id=\"cn.missfresh.application:id/lv_address\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]
loc = driver.find_element(By.ID,'cn.missfresh.application:id/lv_address')
loc.find_element(By.XPATH,'//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]').click()
time.sleep(1)
#选择支付方式
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/confirm_recycler_view\"]/android.widget.RelativeLayout[6]/android.widget.ImageView[2]
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/confirm_recycler_view\"]/android.widget.RelativeLayout[5]/android.widget.ImageView[2]
#//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/confirm_recycler_view\"]/android.widget.RelativeLayout[7]/android.widget.ImageView[2]
driver.find_element(By.XPATH,'//android.widget.RelativeLayout[@resource-id="cn.missfresh.application:id/rl_payment"]/android.widget.ImageView[2]').click()
time.sleep(1)
#点击去支付
driver.find_element(By.ID,'cn.missfresh.application:id/tv_confirm').click()
time.sleep(1)
# #选择与取消全选商品
# driver.find_element(By.ID,'cn.missfresh.application:id/cb_select_all').click()
# time.sleep(1)
# #删除商品
# driver.find_element(By.ID,'cn.missfresh.application:id/tv_delete').click()
# time.sleep(1)
# driver.find_element(By.ID,'cn.missfresh.application:id/tv_ensure').click()
# time.sleep(1)
#退出并关闭驱动
driver.quit()
