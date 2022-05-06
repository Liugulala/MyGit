# 登录页面元素的元素对象及操作
# -*- encoding=utf8 -*-
from util.find_element_util1 import *


# app-googl登录
def login_google():
    logingo = E_login.loginTest
    login = E_login.googl_login
    login = login.click()
    if login != logingo:
        E_login.google.click()
        print(11)
    return


# app-snapchat登录
def login_snapchat():
    snapchat = E_login.snapcha_login
    snapchat.click()
    if snapchat != E_login.button:
        E_login.button.click()
    return


# app-Facebook登录
def login_Facebook():
    Facebook = E_login.facebook_login
    Facebook.click()
    return


'''
#app-Facebook登录
def login_TikTok():
    TikTok =E_login.tiktok_login
    TikTok.click()
    return
'''


# 退出登录
# 点击头像
def Head_home():
    head = E_home.head_home
    head.click()
    return


# 进入banner地图详情
def HomeExperirnce():
    E_home.View_home.click()
    return HomeExperirnce()


# 创建房间
def Experirnceroom():
    if E_home.download_Experirnce:
        E_home.download_Experirnce.click()
    else:
        E_home.joinPublicRoompoco_Experirnce.click()
        pass


Head_home()
