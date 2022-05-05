from page.home_page import *
import os
import subprocess
import multiprocessing
import time

import pytest

# 初级版
# 切换到appium的main.js所在路径
os.chdir(r'C:\Users\Admin\AppData\Local\Programs\Appium'
         r'\resources\app\node_modules\appium\build\lib')

# 执行cmd命令
# os.system('node main.js')
os.system(r'node main.js -p 7890 -g C:\project\python\app_test_project\app_test_06\log')

# 注意点：os.system会堵塞代码继续往下执行

# 执行测试代码（直接这样运行测试时不行的）
pytest.main()


def start_appium():
    """启动appium"""
    # 使用另外的模块
    # appium_server_path = r'C:\Users\Admin\AppData\Local\Programs\Appium' \
    #                      r'\resources\app\node_modules\appium\build\lib\main.js'
    os.chdir(r'C:\Users\Admin\AppData\Local\Programs\Appium'
             r'\resources\app\node_modules\appium\build\lib')
    port = 4723
    appium_log_path = r'C:\project\python\app_test_project\app_test_06\log{}.log'.format(port)
    subprocess.Popen('node main.js -p {} -g {}'.format(port, appium_log_path),
                     stdout=subprocess.STDOUT,
                     stderr=subprocess.PIPE,
                     shell=True).communicate()


if __name__ == '__main__':
    # 创建一个进程去启动appium
    p = multiprocessing.Process(target=start_appium)
    p.start()
    time.sleep(10)
    # 运行测试用例
    pytest.main()

