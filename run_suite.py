# 执行测试套件和生成测试报告

# - 1 导包：unitest，测试用例，os，time
import unittest
from script.employe_params import TestEmployee
from script.login_params import TestLogin
import os,time
# - 提前准备好生成测试报告的HTMLTestRunner_PY3，放在site-packages
# - 2 测试套件
suite = unittest.TestSuite()
# - 3 将测试用例添加导测试套件
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
# - 4 定义报告的名称
report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# - 5 打开报告，使用HTMLTestRunner_PY3执行测试套件，生成测试报告
with open(report_path, mode='wb') as f:
    # 初始化HTMLTestRunner_PY3
    from HTMLTestRunner_PY3 import HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=2, title="人力资源管理系统接口测试报告", description="这是项目实战的报告")
    # 运行测试套件
    runner.run(suite)
