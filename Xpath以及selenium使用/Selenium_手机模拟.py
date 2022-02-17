import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.touch_actions import TouchActions #引入触控类
import time


def web_driver_Chrome():
    '''==========================================================================================='''
    mobileEmulation={'deviceName':'iPhone 6/7/8'}
    '''==========================================================================================='''



    options = webdriver.ChromeOptions()
    '''==========================================================================================='''
    options.add_experimental_option('mobileEmulation',mobileEmulation)
    # 关闭w3c模式！！！非常重要，否则无法点击
    options.add_experimental_option('w3c',False)
    '''==========================================================================================='''

    tar_dri = Service(executable_path=r"F:\Py-Pro\Spider\chromedriver.exe")
    # chrome浏览器主程序位置
    location = r"F:\Py-Pro\Spider\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location

####某些网站会识别selenium
    options.add_experimental_option('excludeSwitches',['enable-automation'])


    driver = webdriver.Chrome(service=tar_dri, options=options)
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/")
    '''==========================================================================================='''
    # 模拟人手点击坐标操作
    action = TouchActions(driver)
    action.tap_and_hold(75, 125).release(75, 125).perform()
    # double_tap
    # 双击
    # filck_element
    # 滑动
    # long_press
    # 长按
    # move
    # 移动
    # perform
    # 执行
    # release
    # 放开
    # scroll
    # 滚动
    # tap
    # 轻点（单击）

    '''==========================================================================================='''

    time.sleep(2)
    driver.quit()


def main():
    try:
        web_driver_Chrome()
    except:
        print("页面好慢的哟")
    pass

if __name__ == '__main__':
    main()
