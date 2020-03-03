# 初始化日志配置的代码，应该放在api.__init__.py中
# 为什么呢？
# 因为，我们后续所有的接口测试操作，都会通过script脚本运行
# 而script脚本会调用api中封装的接口
# 每次调用api的接口时，都会先运行api模块下面的__init__.py文件
# 从而利用这个机制自动地对日志进行初始化操作
# 初始化后，只要是在调用API后的代码，都能够使用logging打印日志

# 导包，导入app模块和日志模块
import app
import logging
# 初始化日志
app.init_logging()
# 测试
logging.info("测试日志是否能够正常打印2！")
