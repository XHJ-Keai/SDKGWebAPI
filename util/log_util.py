import logging

from util.path_util import PathUtil


class LogUtil:
    __log_util = None  # 单例模式标记
    __log_type = logging.INFO  # log类型
    __if_console = True  # 是否控制台打印

    @classmethod
    def set_log_util(cls, if_console=__if_console, log_type=__log_type,
                     log_file=PathUtil.log_file_named_with_current_time()):
        cls.__log_util: LogUtil = LogUtil(if_console=if_console, log_type=log_type, log_file=log_file)

    @classmethod
    def get_log_util(cls, ):
        if cls.__log_util is None:
            cls.__log_util: LogUtil = LogUtil()
        return cls.__log_util

    def __init__(self, if_console=__if_console, log_type=__log_type,
                 log_file=PathUtil.log_file_named_with_current_time()):
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.INFO)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # 控制台输出
        if if_console:
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(log_type)
            self.logger.addHandler(sh)

        # 读入日志文件
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(log_type)
        self.logger.addHandler(fh)

    def debug(self, *messages):
        for message in messages:
            self.logger.debug(message)

    def info(self, *messages):
        for message in messages:
            self.logger.info(message)

    def war(self, *messages):
        for message in messages:
            self.logger.warning(message)

    def error(self, *messages):
        for message in messages:
            self.logger.error(message, exc_info=True)

    def log_graph(self, graph_node_info, graph_version, hint="----graph info----"):
        self.info(hint + graph_version)
        self.info(graph_node_info)

    def log_call_interface(self, user_input):
        self.info(user_input)

