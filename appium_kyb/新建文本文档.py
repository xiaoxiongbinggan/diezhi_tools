from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium_autorun.common.desired_caps import appium_caps
import  logging
import  logging.config
import time
import os


CON_LOG='../config/log.conf'
#读取配置文件传递给常量
logging.config.fileConfig(CON_LOG)
#调用logging的函数读取常量配置文件
logging=logging.getLogger()
#定义一个采集器
class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(self,start_x,start_y,end_x,end_y,duration)
class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cancel=(By.ID,'com.tal.kaoyan:id/view_wemedia_cancel')
    tip_commit=(By.ID,'com.tal.kaoyan:id/tip_commit')
    button_myself = (By.ID,'com.tal.kaoyan:id/mainactivity_button_myself')
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    rightButton = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logoutButton = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    def check_cancelBtn(self):
        logging.info('检测cancel_btn按钮')
        try:
            element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('没有检测到cancel_btn')
        else:
            element.click()
            logging.info('点击了cancel_btn')
    def check_skipBtn(self):
        logging.info('检测skip_btn')
        try:
            element= self.driver.find_element(*self.skipBtn)
            logging.info('检测到cancel_btn')
        except NoSuchElementException:
            logging.info('没有检测到skip_btn')
            TouchAction(self.driver).tap(x=941, y=91).perform()
            logging.info('根据坐标点点击按钮')
        else:
            element.click()
            logging.info('点击了skip_btn')

    def check_advertise(self):

        try:
            adver_btn = self.find_element('com.tal.kaoyan:id/view_wemedia_cacel')
            logging.info('查找广告页')

        except NoSuchElementException:
            logging.info('没有跳出广告')
        else:
            adver_btn.click()
            logging.info('关闭广告')
    def check_account_alert(self):
        logging.info('检查账户是否已经登录')
        try:
            element=self.find_element(*self.tip_commit)
        except NoSuchElementException:
            logging.info('账号没有在登录')
        else:
            logging.info('账号在登录')
            element.click()
    def check_loginStaues(self):
        logging.info('检测账号登录')
        self.check_advertise()
        self.check_account_alert()
        try:
            self.find_element(*self.button_myself).click()
            self.find_element(*self.username)
        except NoSuchElementException:
            logging.error('登录失败')
            self.getScreenShot('登录失败')
            return False
        else:
            logging.info('登录成功')
            return True
    def get_screenSize(self):
        x=self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x,y)
    def swipeLeft(self):
        logging.info('左滑')
        l=self.get_screenSize()
        y1=int(l[1]*0.5)
        x1=int(l[0]*0.95)
        x2=int(l[0]*0.25)
        self.swipe(x1,y1,x2,y1,1000)
    def getTime(self):
        self.now=time.strftime('%Y %M %D %H %M %S')
        return self.now
    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('get %s screenshot'%module)
        self.driver.get_screenshot_as_file(image_file)
    # def get_csv_data(self,csv_file,line):
    #     csv_file=csv.reader(open(csv_file,'r',encoding='UTF-8'))
    #     for i,row in enumerate(csv_file):
    #         if i == line:
    #             return row
    def get_size(self):
        x=self.get_window_size()['width']
        y = self.get_window_size()['height']
        return x,y



if __name__ == '__main__':
    driver=appium_caps()
    com=Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()
    username = 'qinyujie1'
    password = 'qinyujie1'
    email = 'qinyujie1' + '@163.com'
