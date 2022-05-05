# 登录页面元素的元素对象及操作
# -*- encoding=utf8 -*-
from conf.By_Element_conf import *
from conf.Home_conf import E_home
from util.screenshot_util1 import *
from util.find_element_util1 import *
#app登录
def login(dengl):
    button=E_login.button
    loginTest=E_login.loginTest
    logong=E_login.googl_login
    if loginTest:
        E_logint=E_login.google
        E_logint.click()
    elif button:
        wE_login=E_login.button
        wE_login.click()
        pass
    return login

#退出登录
def Exit():
    E_home.head_home.click()
    E_Private.setting_Private.click()
    E_Private.logout_Private.click()
    snapshot(Filename='123',msg="登录")
    E_Private.Yes_Private.click()


login(E_app.master)

