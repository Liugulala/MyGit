#首页元素
from conf.module import poco
class E_home():

    #首页地图
    View_home=poco(text="View") #进入到地图详情
    '''----------------------------------------------------------'''
    #首页头部展示
    head_home = poco(name="com.pointone.buddyglobal.alpha:id/headImage")#头像
    search_home = poco(name="com.pointone.buddyglobal.alpha:id/iv_homepage_search ")#搜索
    Explore_home = poco(name="android:id/text1")#Explore
    ForYou_home = poco(name="com.pointone.buddyglobal.alpha:id/headImage")#For You
    friend_home = poco(name="com.pointone.buddyglobal.alpha:id/headImage")#添加好友
    inform_home = poco(name="com.pointone.buddyglobal.alpha:id/notificationIcon")#通知

    '''----------------------------------------------------------'''
    #首页底部tab
    Tap_to = poco(text="Tap to create") #登录-跳转草稿箱引导按钮
    homeicon = poco(name="com.pointone.buddyglobal.alpha:id/homeIcon")#首页home按钮
    propsicon = poco(name="com.pointone.buddyglobal.alpha:id/propsStoreLayout")#素材按钮
    createIcon = poco(name="com.pointone.buddyglobal.alpha:id/createIcon")#草稿箱
    feedIcon = poco(name="com.pointone.buddyglobal.alpha:id/feedIcon")  # feed
    IMIcon = poco(name="com.pointone.buddyglobal.alpha:id/chatIcon")  # IM

    '''----------------------------------------------------------'''
    #地图详情。
    download_Experirnce = poco(name="com.pointone.buddyglobal.alpha:id/download")#地图未渲染过
    joinPublicRoompoco_Experirnce=poco(name="com.pointone.buddyglobal.alpha:id/joinPublicRoom")#创建公共房间
    joinPrivateRoom_Experirnce=poco(name="com.pointone.buddyglobal.alpha:id/joinPrivateRoom")#创建私人房间

    '''----------------------------------------------------------'''
    #进房
