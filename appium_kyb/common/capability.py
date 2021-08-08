import yaml

from appium import webdriver


with open(r'E:\py\appium_kyb\config\capability_huawei.yaml', 'r') as file:
    data = yaml.load(file,Loader=yaml.FullLoader)

    driver=webdriver.Remote('127.0.0.1:4723/wd/hub', data)




