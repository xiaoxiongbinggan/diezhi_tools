# coding: utf-8
import uiautomator2 as u2
# import capability
d=u2.connect_usb('3EP7N18929000892')
#


d(text="考研帮").click()
d(resourceId="com.tal.kaoyan:id/login_email_edittext").click()
d.send_keys("qinyujie", clear=True)
d(resourceId="com.tal.kaoyan:id/login_password_edittext").click()
d.send_keys("123", clear=True)
d(resourceId="com.tal.kaoyan:id/login_login_btn").click()