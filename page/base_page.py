'''
activity基类
'''
import random
import time

from driver.driver import get_driver
from system_element import BASE_PATH


class BasePage():

    def __init__(self, driver):
        '''
        初始化,App的初始化，其他属性初始化
        :param driver: App的webdriver对象
        '''
        self.driver = driver

    def find_element(self, loc):
        '''
        控件的定位方法
        :param loc: 定位信息：(By.ID, 'value')
        :return: 被定为的控件对象
        '''
        return self.driver.find_element(*loc)

    def assert_text(self, loc):
        '''
        获取控件的文本信息，可用于进行断言
        :param loc: 控件的定位信息：(By.ID, 'value')
        :return: 被定为的控件的文本信息
        '''
        ret = self.find_element(loc).text
        print('获取断言')
        return ret

    def screenshot(self, func_name):
        '''
        截图,会在项目中的report文件夹下的image下进行保存
        :param func_name:  调用的方法的名称
        '''
        # 获取时间并进行格式化
        start_time = time.strftime('%Y%m%d %H%M%S')
        # 拼接文件路径
        filepath = '{}\\report\\image\\{}_{}.png'.format(BASE_PATH, func_name, start_time)
        self.driver.save_screenshot(filepath)
        print('截图')

    def quit(self):
        '''退出app'''
        self.driver.quit()
        print('退出app')

    def swipe_to(self,direction='up',count=1):
        '''滑动'''
        #获取窗口大小
        size = self.driver.get_window_size(windowHandle='current')
        x1 = size["width"]*0.2
        y1 = size["height"]*0.7
        x2 = size["width"]*0.5
        y2 = size["height"]*0.5
        x3 = size["width"]*0.7
        y3 = size["height"]*0.2
        #利用窗口大小设置滑动值
        for i in range(count):
            if direction == 'up':
                self.driver.swipe(x2,y1,x2,y2)
                time.sleep(1)
            elif direction == 'left':
                self.driver.swipe(x2, y2, x1, y2)
                time.sleep(1)
            elif direction == 'right':
                self.driver.swipe(x2, y2, x3, y2)
                time.sleep(1)
            elif direction  == 'down':
                self.driver.swipe(x2, y3, x2, y2)
                time.sleep(1)
            print('这是第%d次%s滑动'%(i+1,direction))

    def get_element_random(self, floc, cloc, last_loc='1'):
        '''
        通过上级定位符和下级的list定位符获取控件列表中的某个控件对象,随机获取
        :param floc: 父级定位器，可唯一定位
        :param cloc: 下级list定位器：(By.ID, 'value')
        :param clast_loc: 第三个参数，布局下的最小一个控件定位器
        :return: 列表中的一个随机控件对象，传递last_loc后返回布局下的一个最小控件
        '''
        # 判断入参是否为空
        # if floc is None or cloc is None:
        #     raise ValueError('上级定位符或list的定位符不能为空')

        f_element = self.find_element(floc)
        elements = f_element.find_elements(*cloc)
        list_len = len(elements)
        rand = random.randint(0, list_len - 1)
        if last_loc == '1':
            return elements[rand]
        else:
            last_ele = elements[rand].find_element(*last_loc)
            return last_ele

    def get_element(self, floc, cloc):
        '''
        从父类往下递归找符合条件的控件
        :param floc: 父级定位器：ID
        :param cloc: 子定位器：className
        :return: 列表中的一个随机控件对象
        '''
        ele = self.driver.find_element_by_android_uiautomator('new '
                                                              'UiSelector().resourceId("{}").fromParent('
                                                              'new UiSelector().Id("{}"))'.format(floc, cloc))
        return ele



