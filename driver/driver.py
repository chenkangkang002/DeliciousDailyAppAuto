'''
得到对应App的驱动
'''
from appium import webdriver

def get_driver(appPakage='cn.missfresh.application',
               appActivity='cn.missfresh.module.base.main.view.SplashActivity'):
    '''
    根据传入的app包名和app的activity名称进行不同程序的初始化
    :param appPakage: 程序的包名
    :param appActivity: 程序的activity
    :return:
    '''
    desired_capabilities = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': '127.0.0.1:62001',
        'appPackage': appPakage,
        'appActivity': appActivity,
        'unicodeKeyboard': True,    #开启Unicode输入法，保证输入稳定
        'resetKeyboard': True,      #unicode输入结束后，重置输入法
        'newCommandTimeout':600,    #appium服务等待发送新消息的时间
        'noReset': True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(30)
    return driver
