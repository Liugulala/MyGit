#全局变量
from airtest.core.api import *
auto_setup(__file__)
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco#安卓
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)#安卓
