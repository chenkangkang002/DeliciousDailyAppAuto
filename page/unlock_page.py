import time
from appium.webdriver.common.touch_action import TouchAction
from driver.driver import get_driver
from page.base_page import BasePage

def unlock(driver,passwd):
    #driver = get_driver()      #实例化get_driver方法并赋值给driver
    ta = TouchAction(driver)
    driver.swipe(200, 500, 200, 200, 200)  # 向上滑动，弹出九宫格
    time.sleep(2)
    p = [[232, 956], [445, 956], [661, 956],  # 将九个点的坐标写上，并封装成一个列表
        [232, 1174], [445, 1174], [661, 1174],
        [232, 1392], [445, 1392], [661, 1392]]
    ta.press(x=p[passwd[0]][0], y=p[passwd[0]][1])  # 通过索引找到第一个点按压
    ta.wait(1000)
    for n in passwd[1:]:  # 通过循环取值
        ta.move_to(x=p[n][0], y=p[n][1])
    ta.release()  # 释放
    ta.perform()  # 提交

# passwd = [0, 1, 2, 5, 4, 3, 6, 7, 8]  # 确定密码的排列顺序
# unlock(passwd)
