import unittest
from driver.driver import get_driver
from page.base_page import BasePage
from page.unlock_page import unlock


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        print('初始化')

    def tearDown(self):
        quit = BasePage(self.driver)  # 实例化BasePage
        quit.quit()  # 调用BasePage的quit()方法
        print('清理：退出')