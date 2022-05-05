#包名
from conf.module import poco


class E_app():
    master=("com.pointone.buddyglobal.debug")  # mastae测试包
    alpha=("com.pointone.buddyglobal.alpha")  # alpha测试包
    app=("com.pointone.buddyglobal")  # 线上包

class E_login():
    #登录
    snapcha_login = poco(name="com.pointone.buddyglobal.alpha:id/snapchatBtn")#snapchatBtn
    button = poco(name="com.snapchat.android:id/login_kit_auth_continue_button")#继续
    facebook_login = poco(name="com.pointone.buddyglobal.alpha:id/facebookBtn")#facebookBtn
    googl_login = poco(name="com.pointone.buddyglobal.alpha:id/googleBtn")#googleBtn
    loginTest = poco(text="选择帐号")#选择帐号
    google = poco(text="liuliwen30@gmail.com")#添加google账号
    tiktok_login = poco(name="com.pointone.buddyglobal.alpha:id/tiktokBtn")#tiktokBtn
#   lgoinsnapchatBtn=poco(name="com.pointone.buddyglobal.alpha:id/snapchatBtn")#snapchatBtn

    #登出
class E_Private():
    setting_Private=poco(name="com.pointone.buddyglobal.alpha:id/setting")#设置按钮
    logout_Private=poco(name="com.pointone.buddyglobal.alpha:id/logOutLayout")#退出入口
    setting_Privatee=poco(name="com.pointone.buddyglobal.alpha:id/setting")#确认按钮弹窗
    Yes_Private=poco(text="Yes")#yes
    NO_Private=poco(text="NO")#no


