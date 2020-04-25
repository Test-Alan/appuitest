import os
import socket
from sys import platform
from Utils.logger import logger


def check_port(host, port):
    """
    检查指定端口是否被占用
    :param host: 主机地址
    :param port: 端口号
    :return: Boolean
    """
    if isinstance(port, str):
        port = int(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError as msg:
        # 未占用
        logger.info("port {} is available".format(port))
        return True
    else:
        # 已占用
        logger.info("port {} already be in use".format(port))
        return False


def release_port(port):
    """
    释放端口
    :param port: 端口号
    :return:
    """
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        cmd = "lsof -i tcp:%s | awk '$9 eq \"%s\" && $10==\"(LISTEN)\"{print $2}'" %(port, port)
        pid = os.popen(cmd).read()
        logger.info(f"appium pid: {pid}")
        cmd_kill = f"kill -9 {pid}"
    else:
        cmd = f"netstat -ano | findstr {port}"
        logger.info(cmd)
        result = os.popen(cmd).read()
        if str(port) and "LISTENING" in result:
            index = result.index("LISTENING")
            start = index + len("LISTENING") + 7
            end = result.index("\n")
            pid = result[start:end]
            cmd_kill = f"taskkill -f -pid {pid}"

    logger.info(f"kill appium pid: {cmd_kill}")
    os.popen(cmd_kill)


if __name__ == '__main__':
    print(check_port("127.0.0.1", 4723))
    release_port(4723)


