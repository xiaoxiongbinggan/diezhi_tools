from appium_kyb.common.capability import driver
from selenium.common.exceptions import NoSuchElementException





def first_guide():

    try :
        button1 = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no updata button')
    else:
        button1.click()

    try :
        button2 = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')

    except NoSuchElementException:
        print('no skip button')
    else:
        button2.click()




if __name__ == '__main__':
  first_guide()
