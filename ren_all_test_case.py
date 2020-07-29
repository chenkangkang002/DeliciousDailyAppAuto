'''
运行所有的test_case
'''
import time
import unittest

#筛选执行用例
from BeautifulReport import BeautifulReport

from system_element import BASE_PATH

discover = unittest.defaultTestLoader.discover(start_dir='test_case',
                                    pattern='test_*.py',
                                    top_level_dir=None)
#实例化BeautifulReport
report = BeautifulReport(discover)
#执行测试用例
#格式化时间
start_time = time.strftime('%Y%m%d %H%M%S')
#文件名
filename =  'DeliciousDailyApp_{}.html'.format(start_time)
#文件保存路径
filepath = '{}/report'.format(BASE_PATH)
#用例执行
report.report(description='每日优鲜App自动化测试报告',
              filename=filename,
              log_path=filepath)