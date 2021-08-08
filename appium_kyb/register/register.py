import appium
import logging.config
from appium_kyb.first_guide import enterapp_guide
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium_kyb.common.capability import *#调用启动appium的模块
import random
# import logging
# logging.config.fileConfig(r'C:\Users\Admin\Desktop\study\py\appium\config\log.conf')
# logging.getLogger()

def register():
    webdriver.WebElement.find_element_by_id('com.tal.kaoyan:id/login_register_username_edittext').send_keys('qinyujie'+str(random.randint(1000,9000)))

    webdriver.WebElement.find_element_by_id("com.tal.kaoyan:id/login_register_password_edittext").send_keys('qinyujie'+str(random.randint(1000,9000)))

    webdriver.WebElement.find_element_by_id("com.tal.kaoyan:id/login_register_email_edittext").send_keys('qinyujie' + str(random.randint(1000, 9000)))


    register_btm=webdriver.WebElement.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()


if __name__ == '__main__':
    # enterapp_guide()
    register()