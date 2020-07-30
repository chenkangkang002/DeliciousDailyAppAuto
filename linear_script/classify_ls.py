'''
分类activity的线性脚本
'''
from selenium.webdriver.common.by import By

from driver.driver import get_driver


def disagree_treaty():
    '''不同意进入的隐私协议'''
    driver = get_driver()   #调用App驱动并启动App
    driver.find_element(By.ID, 'cn.missfresh.application:id/tv_double_btn_cancel').click()

def agree_treaty():
    '''同意进入的隐私协议'''
    driver = get_driver()  # 调用App驱动并启动App
    driver.find_element(By.ID, 'cn.missfresh.application:id/tv_double_btn_ok').click()

def classify_activity_search_add_cart():
    '''首次进入App，分类页面搜索之后加入购物车'''
    driver = get_driver()  # 调用App驱动并启动App
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'cn.missfresh.application:id/classifyTab').click()   #点击分类
    # driver.find_element(By.ID, 'cn.missfresh.application:id/tv_next').click()   #点击导航下一步
    # driver.find_element(By.ID, 'cn.missfresh.application:id/tv_end').click()    #点击我知道了
    driver.find_element(By.ID, 'cn.missfresh.application:id/tv_sales_count').click()    #点击销量
    driver.find_element(By.ID, 'cn.missfresh.application:id/tv_sales_count').click()  # 点击销量
    driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/recycler_view\"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]') #点击添加到购物车+
    driver.find_element(By.ID, 'cn.missfresh.application:id/search_layout').click() #点击搜索
    driver.find_element(By.ID, 'cn.missfresh.application:id/search_view').clear()   #清理输入框
    driver.find_element(By.ID, 'cn.missfresh.application:id/search_view').send_keys('牛肉干')  #输入搜索内容
    driver.press_keycode('66')  #回车
    driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/result_recycler\"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()    #添加第一个商品到购物车
    driver.find_element(By.ID, 'cn.missfresh.application:id/search_back_view')  #点击返回分类activities
    driver.quit()
# //androidx.recyclerview.widget.RecyclerView[@resource-id=
# \"cn.missfresh.application:id/result_recycler\"]" \
#  "/android.widget.RelativeLayout[2]
# //androidx.recyclerview.widget.RecyclerView[@resource-id=
# \"cn.missfresh.application:id/result_recycler\"]" \
#  "/android.widget.RelativeLayout[1]/android.widget." \
#  "FrameLayout[2]/android.widget.RelativeLayout[2]/" \
#  "android.widget.FrameLayout[1]/android.widget.ImageView[1]
classify_activity_search_add_cart()