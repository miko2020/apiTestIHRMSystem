# 存放全局变量，公有的配置函数或者类
import logging
import os
from logging import handlers

# 获取当前项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 定义全局变量headers
HEADERS = {"Content-Type":"application/json"}
EMPID = ""
# 1 定义一个初始化日志配置的函数：初始化日志的输出路径（例如：输出到控制和日志文件中）
def init_logging():
    # 2 创建日志器
    logger = logging.getLogger()
    # 3 设置日志等级:Debug,Info,Warn,Error,critical
    logger.setLevel(logging.INFO)
    # 4 创建处理器，通过处理控制日志的打印（打印到控制台和日志文件中）
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器：文件处理的作用是把日志写道日志文件当中，如果我们不管理日志文件，那么日志文件会越来越大
    # 这种情况下，我们需要拆分日志，按大小拆分和按时间拆分（掌握按时间拆分），使用logging模块中的拆分日志的工具来进行
    # when='S', interval=10 代表两次运行的间隔时间超过10秒就会拆分日志
    # backupCount:保留的日志文件数量
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/ihrm.log",
                                                   when='S',
                                                   interval=10,
                                                   backupCount=3,
                                                   encoding='utf-8')
    # 5 设置日志的格式，所以需要创建格式和格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 6 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)


if __name__ == '__main__':
    # 初始化日志配置时，由于没有返回日志器，所以这个配置函数中的全部配置都会配置到logging的root节点
    init_logging()
    # 既然初始化到了root节点，那么我们可以就直接使用logging模块打印日志
    logging.info("测试日志会不会打印!")
