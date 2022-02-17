import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     # 引入键盘按键包
from selenium.webdriver.common.action_chains import ActionChains    #引入鼠标按键包

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.touch_actions import TouchActions
import time


def web_driver_Chrome():
    ##调用系统默认浏览器
    # driver = webdriver.Chrome("F:\Py-Pro\Spider\chromedriver.exe")
    # driver.get("http://www.baidu.com")
    # time.sleep(10)
    # driver.quit()

    ##指定调用某个chrome
    options = webdriver.ChromeOptions()
    tar_dri = Service(executable_path=r"F:\Py-Pro\Spider\chromedriver.exe")
    # chrome浏览器主程序位置
    location = r"F:\Py-Pro\Spider\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location

    '''==========================================================================================='''
#### 增加user-agent
    options.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')

    '''==========================================================================================='''
# ##使用手机浏览
#     #设置手机型号
#     mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
#         """#第二种手机型号设置方法
#         mobileEmulation = {
#             "deviceMetrics":{
#                 "width":350,
#                 "height":200,
#                 "pixelRatio":3.0,
#                 "touch":False
#             }
#         }"""
#
#     #使用某个手机型号浏览
#     options.add_experimental_option('mobileEmulation',mobileEmulation)
    '''==========================================================================================='''

# ####使用静默模式（不跳出浏览器还去操作）
#     options.add_argument("headless")
    '''==========================================================================================='''

# ####加代理 http https socks4 socks5
#     options.add_argument('--proxy-server=%s'%'socks5://127.0.0.1:10808')
    '''==========================================================================================='''

# ####更改浏览器的语言
#     options.add_argument('--lang=en-US')
    '''==========================================================================================='''
####某些网站会识别selenium
    options.add_experimental_option('excludeSwitches',['enable-automation'])

    '''==========================================================================================='''
# #### 图片不加载(访问速度巨快)
#     prefs = {
#         'profile.default_content_setting_values': {
#             'images': 2
#         }
#     }
#     options.add_experimental_option('prefs', prefs)

    '''==========================================================================================='''
    '''==========================================================================================='''

    driver = webdriver.Chrome(service=tar_dri, options=options)

    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''
    '''==========================================================================================='''


    ##使用get方法打开一个网站
    # driver.get("http://www.4399dmw.com/donghua/")
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/")
    # driver.get("http://127.0.0.1/tese.html")
    '''==========================================================================================='''
# ####超时操作系列
# ##如果10s界面还没加载出来，就抛出一个异常，需要配合try来做
#     driver.set_page_load_timeout(10)
#
# ##隐性等待，全局查找页面元素的等待时间，如果这个时间没找到指定元素，就抛出异常(全局做一次就好了)
#     driver.implicitly_wait(10)
#
# ##显性等待(使用频率最高的元素超时设置)
#     WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,'j-anime-nav'))
#     # until用来检测指定的元素是否出现，如果在超时的时间内出现就返回选择器的信息，否则报TimeOutException
#     # until_not用来检测指定的元素是否消失，如果在超时时间内消失返回True，否则报TimeOutException
#
#     # 如果20s内页面加载的title是这个，就返回true，不是就报错
#     a = WebDriverWait(driver, 20).until(EC.title_is(u'热血动画片/动画电影-热血动画搜索-4399动画片大全'))
#     print(a)
#
#     # 如果20s内页面加载的title是包含这个，就返回true，不是就报错
#     a = WebDriverWait(driver, 20).until(EC.title_contains(u'动画片'))
#
#     # 如果20s内class='lst'被加载出来就返回true并且继续执行，不是就报错
#     a = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'lst')))
#
#     # 如果20s内id='kw'的元素被可见（高宽都>0），那么就true继续执行，不是就报错
#     a = WebDriverWait(driver, 20).until(EC.visibility_of(driver.find_element(by=By.ID, value='kw')))
#
#     # 如果20s内匹配xpath语法中的文字是某个，就返回true并且继续执行，不是就报错
#     a = WebDriverWait(driver, 20).until(
#         EC.text_to_be_present_in_element((By.XPATH, "//div[@class='lst']/a[3]/div/p"), u'吃鸡大作战'))

    '''==========================================================================================='''
    # ##清除input标签所有的value
    # sell1 = driver.find_element_by_xpath("//input[@id='j-input']")
    # driver.execute_script("arguments[0].value='';", sell1)

# ##根据id找到对应目标，并且输入内容
# driver.find_element(By.ID,"j-input").send_keys("蜡笔")
# ##找到按钮
# driver.find_element(By.XPATH,"//button[@class='banner__btn']").click()
# ##获取当前页面地址#虽然点击，但并未切换标签页，仍停留原界面，url没变化
# print(driver.current_url)

#####获取当前页面源码
    '''可以考虑借此进行BS格式化来更好的爬取数据'''
    # print(driver.page_source)

# ####获取当前页面cookie
#     #查看cookie
#     cookie=driver.get_cookies()
#     print(cookie)
#     #增加cookie
#     driver.add_cookie({'name':'xiaoming','key':'1111'})
#     #清除所有cookie
#     driver.delete_all_cookies()
    '''==========================================================================================='''

# ####浏览器操作
#     driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/")
#     time.sleep(1)
#     driver.get("http://www.4399dmw.com/dh/nzjshi/")
#     #后退
#     driver.back()
#     time.sleep(2)
#     #刷新
#     driver.refresh()
#     #前进
#     driver.forward()
#     ##最大化
#     driver.maximize_window()
    '''==========================================================================================='''

    '''==========================================================================================='''

##点击下一页
# driver.find_element(By.XPATH,"//a[contains(text(),'下一页')]").click()
    '''==========================================================================================='''

# ####新建标签页
#     js = 'window.open("http://www.baidu.com")'
#     driver.execute_script(js)
#     print(driver.current_url)
# ####切换选项卡
#     driver.switch_to.window(driver.window_handles[1])
#     print(driver.current_url)
# ####切换回原来的
#     driver.switch_to.window(driver.window_handles[0])
# #### 关闭当前切到的标签
#     driver.close()
#
# #####看到当前有多少个窗口并且句柄是什么
#     print(driver.window_handles)
    '''==========================================================================================='''

# ####拖动滑块操作
#     #拖到底部（值为0即为顶部）
#     js="document.documentElement.scrollTop=10000"
#     driver.execute_script(js)
    '''==========================================================================================='''

# ####截图操作
#     #页面截图（眼前的页面）
#     driver.get_screenshot_as_file("./a.jpg")
#     #图片转base64：于html文本中img包含：<img src="data:image/jpeg;base64,[a的内容]"/>,即可看到图片
#     a=driver.get_screenshot_as_base64()
#     print(a)
#     #指定位置的截图
#     pic=driver.find_element(By.XPATH,"//div[@class='lst']/a[2]")
#     pic.screenshot('./哪吒.png')

    '''==========================================================================================='''

    '''==========================================================================================='''
    '''==========================================================================================='''
# ####键盘按键包
#     driver.find_element(By.ID, "j-input").send_keys("蜡笔")
# # 组合键输入：ctrl+a
#     driver.find_element(By.ID, "j-input").send_keys(Keys.CONTROL, 'a')
# ====================================================================
# ####鼠标按键包
#     #移动鼠标并点击
#     action=ActionChains(driver).move_by_offset(70,120).click()
#     #开始执行action操作
#     action.perform()
#     #鼠标移回左上角并且执行
#     ActionChains(driver).move_by_offset(-70,-120).perform()
#
# #####获取登录的位置，发现一个是link的，文字是text的element
#     denglu=driver.find_element(By.LINK_TEXT,"登录")
# ####鼠标悬停
#     ActionChains(driver).move_to_element(denglu).perform()
#
# ####    鼠标点击的第一种方法：
#     #找到logo的位置
#     logo = driver.find_element(By.XPATH,"//div[@class='banner__main']/a")
#     # 执行点击
#     ActionChains(driver).click(logo).perform()
# ####    鼠标点击的第二种方法：
#     # 找到logo的位置
#     logo = driver.find_element(By.XPATH, "//div[@class='banner__main']/a")
#     denglu = driver.find_element_by_xpath("//a[contains(text(),'登录')]")
#     # 执行点击
#     action=ActionChains(driver)
#     action.click(logo)
#     time.sleep(2)
#     action.click(denglu)
#     action.perform()
# #### 拖拽操作(手机端较适合)
#     first_tar = driver.find_element_by_xpath("//span[contains(text(),'魔幻陀螺')]")
#     second_tar = driver.find_element_by_xpath("//a[contains(text(),'动画')]")
#     action = ActionChains(driver)
#     action.drag_and_drop(first_tar, second_tar).perform()
#     #拖拽操作需要使用xpath或者其他方法找到起始位置和终点位置
# #### 鼠标点击像素操作
#     # 把鼠标移动到某个特定的地方，然后点击执行
#     ActionChains(driver).move_by_offset(200, 300).click().perform()
#     # 记得把鼠标移动回来
#     ActionChains(driver).move_by_offset(-200, -300).perform()
# ####鼠标其他操作
#     click()    # 点击鼠标左键
#     click_and_hold() # 点住鼠标左键不放
#     context_click() # 点击鼠标右键
#     double_click() # 双击鼠标左键
#     drag_and_drop_by_offset(first_tar, 100, 100)  # 拖拽到某个坐标然后松开
#     key_down("a") # 按下一个键
#     key_up("a") # 抬起一个键
#     move_to_element(ele)  # 移动到某个元素的位置
#     move_to_element_with_offset(ele, 100, 0) # 移动到某个元素的相对xx的位置（以找到元素的左上角作为0）
# ####如果碰到了下拉框
#     from selenium.webdriver.support.ui import Select
#     # 使用select包裹起来xpath查找到的select元素
#     select1 = Select(driver.find_element(By.XPATH,"//select[@class='year']"))
#     # 选择值是1999的
#     select1.select_by_value("1999")

    '''==========================================================================================='''
    '''==========================================================================================='''

# ####选择多个元素爬取
#     for page in range(14):
#         print("==========================================================================\n"+"--Page%d--"%(page+1))
#         res=driver.find_elements(By.XPATH,"//div[@class='lst']/a/div/p")
#         for i in range(len(res)):
#             print(res[i].text)
#         driver.find_element(By.XPATH, "//a[contains(text(),'下一页')]").click()
#         print("==========================================================================")
# ####获取目标元素的html代码
#     html=driver.find_element(By.XPATH, "//a[contains(text(),'下一页')]").get_attribute("outerHTML")
#     print(html)
# #### 获取目标的css属性
#     html = driver.find_element_by_xpath("//a[contains(text(),'下一页')]").value_of_css_property("background-image")
#     print(html)
# ####获取标签下的文字
#     res=driver.find_elements(By.XPATH,"//div[@class='u-ct']")
#     for i in range(len(res)):
#         title=res[i].find_element(By.XPATH,"./p[@class='u-tt']").get_attribute('innerText')
#         print(title)
    '''==========================================================================================='''

# ####关于iframe的处理
#     ##方法1：
#     # 寻找到iframe的位置
#     find_div_ifr=driver.find_element(By.CSS_SELECTOR,"#outside>iframe")
#     # 让driver切换到iframe所代表的网页中
#     div_ifr=driver.switch_to.frame(find_div_ifr)
#     ##方法2：
#     #可能出现多个iframe
#     find_div = driver.find_elements(By.TAG_NAME,"iframe")
#     # # 让driver切换到第2个iframe中
#     driver.switch_to.frame(find_div[1])
#     #### 释放iframe，回到主页面上
#     driver.switch_to.default_content()
    '''==========================================================================================='''

# ####处理弹窗
#     driver.switch_to.alert.accept()

    time.sleep(2)
    ####关闭webdriver
    driver.quit()


def main():
    try:
        web_driver_Chrome()
    except:
        print("页面好慢的哟")
    pass

if __name__ == '__main__':
    main()
