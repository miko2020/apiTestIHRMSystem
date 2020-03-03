# 导包
import unittest, logging, requests
from api.login_api import LoginApi
from utils import assert_common_utils, read_login_data
from parameterized.parameterized import parameterized

# 创建登陆的测试类，并集成unittest.TestCase
class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 创建登陆的测试函数
    @parameterized.expand(read_login_data)
    def test01_login(self, mobile, password, http_code, success, code, message):
        # 调用登陆接口
        response = self.login_api.login(mobile, password)
        # 打印结果
        logging.info("参数化登陆的结果为：{}".format(response.json()))
        # 断言登陆结果
        assert_common_utils(self, response, http_code, success, code, message)
