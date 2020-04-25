import time

from utils.handle_yaml import read_yaml
from utils.logger import logger
from utils.handle_port import check_port, release_port
from settings import CAPS_DIR
from appium import webdriver
from settings import LOG_DIR
import subprocess
import os


class BaseDriver:
    """
    公共的base_driver类
    """

    def __init__(self, device_info, host="127.0.0.1"):
        self.device_info = device_info
        self.host = host

    def start_appium(self):
        port = self.device_info["server_port"]
        if not check_port(self.host, port):
            release_port(port)
            time.sleep(2)
        cmd = "appium -p {0} -bp {1}".format(self.device_info["server_port"],
                                             self.device_info["server_port"] + 1)
        logger.info(f"start appium server: {cmd}")
        out_path = os.path.join(LOG_DIR, 'appiumlog', str(self.device_info["server_port"]) + ".log")
        subprocess.Popen(cmd, shell=True, stdout=open(out_path, 'a'), stderr=subprocess.STDOUT)

    def get_driver(self):
        desired_caps = read_yaml(CAPS_DIR)
        # desired_caps["platformVersion"] = self.device_info["platform_version"]
        desired_caps["deviceName"] = self.device_info["device_name"]
        desired_caps["systemPort"] = self.device_info["system_port"]
        logger.info(f'http://127.0.0.1:{self.device_info["server_port"]}/wd/hub')
        driver = webdriver.Remote(f'http://{self.host}:{self.device_info["server_port"]}/wd/hub', desired_caps)
        driver.implicitly_wait(5)

        return driver