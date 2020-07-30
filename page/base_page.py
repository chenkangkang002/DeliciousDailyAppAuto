'''
activity基类
'''
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
        filepath = '{}\\report\\image\\{}_{}.html'.format(BASE_PATH, func_name, start_time)
        self.driver.save_screenshot(filepath)
        print('截图')

    def quit(self):
        '''退出app'''
        self.driver.quit()
        print('退出app')


