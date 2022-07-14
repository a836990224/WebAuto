# -*- coding = utf-8 -*-
# @Time : 2022/06/09 17:47
# @Author :Chilong
# @Fil: test_selenium.py
# @Software : PyCharm

import unittest
from Web_cases.Test_case import Testlogin
from Web_cases.Test_case import Test_shujujiansuo
from test_reports import HTMLTestRunnerNew

#1、收集其他文件 当中的测试用例 --TestSuite -- 存放测试用例
s = unittest.TestSuite()
s.addTest(Testlogin('test_login_failed'))  #类名  ('用例名称‘)
s.addTest(Testlogin('test_login_success'))
s.addTest(Test_shujujiansuo('test_sjjs_tongji_success'))
s.addTest(Test_shujujiansuo('test_sjjs_tongji_guiji_success'))

#2、运行测试用例，并生成html的测试报告 - 运行TestSuite

#html文件，支持写入
fs = open('my_report.html', 'wb')
runner = HTMLTestRunnerNew.HTMLTestRunner(fs,title='啊朗的web用例测试报告')
runner.run(s)