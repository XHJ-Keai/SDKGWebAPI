import time
from pathlib import Path

from definitions import DATA_DIR, OUTPUT_DIR


class PathUtil:
    """
    provide a way to get a path of some common objects
    """

    @classmethod
    def log_file(cls, log_file_name="test_log"):
        """
        获取一个可以写log的文件名
        :param log_file_name:
        :return:
        """
        output_dir_log = Path(OUTPUT_DIR) / "log"
        output_dir_log.mkdir(exist_ok=True, parents=True)
        return str(output_dir_log / "{name}.log".format(name=log_file_name))

    @classmethod
    def log_file_named_with_current_time(cls, ):
        """
        获取一个可以写log的文件名,名字包含当前的时间
        :return:
        """
        output_dir_log = Path(OUTPUT_DIR) / "log"
        output_dir_log.mkdir(exist_ok=True, parents=True)
        log_file_name = time.strftime("%Y%m%d-%H-%M", time.localtime())
        return str(output_dir_log / "{name}.log".format(name=log_file_name))


    @staticmethod
    def graph_data(pro_name, version):
        graph_data_output_dir = Path(DATA_DIR)
        graph_data_output_dir.mkdir(exist_ok=True, parents=True)

        graph_data_path = str(graph_data_output_dir / "{pro}.{version}.graph".format(pro=pro_name, version=version))
        return graph_data_path

    @staticmethod
    def trie(pro_name, version):
        trie_output_dir = Path(DATA_DIR)
        trie_output_dir.mkdir(exist_ok=True, parents=True)

        trie_data_path = str(trie_output_dir / "{pro}.{version}.trie".format(pro=pro_name, version=version))
        return trie_data_path


