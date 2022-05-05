# 登录页面元素的元素对象及操作
# -*- encoding=utf8 -*-
from conf.By_Element_conf import *
from conf.Home_conf import E_home
from util.screenshot_util1 import *
from util.find_element_util1 import *
#app登录
def login(denglu):
    return

#退出登录
def Exit():
    return

#进入banner地图详情
def HomeExperirnce():
    E_home.View_home.click()
    return HomeExperirnce()

#创建房间
def Experirnceroom():
    if E_home.download_Experirnce:
        E_home.download_Experirnce.click()
        return
    else :
        E_home.joinPublicRoompoco_Experirnce.click()
        return




