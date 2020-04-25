# coding=utf-8
import os
import time
import pytest
import click
from settings import REPORT_DIR
from settings import cases_path, rerun
from utils.logger import logger
from multiprocessing import Pool

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python3 run_tests.py  (回归模式，生成HTML报告)
  > python3 run_tests.py -m debug  (调试模式)
'''

device_infos = [
            {"platform_version": "5.1.1","device_name": "mumu"}
        ]

def init_env(now_time):
    """
    初始化测试报告目录
    """
    report = os.path.join(REPORT_DIR, now_time)
    os.mkdir(report)
    os.mkdir(os.path.join(report, "image"))


def run_pro(device_info):
    logger.info("回归模式，开始执行✈✈！")
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S") + "-" +str(device_info['server_port'])
    init_env(now_time)

    html_report = os.path.join(REPORT_DIR, now_time, "html")
    xml_report = os.path.join(REPORT_DIR, now_time, "xml")
    pytest.main([f"--cmdopt={device_info}",
                 "-s", "-v",
                 "--alluredir=" + xml_report,
                 cases_path,
                 "--reruns", rerun])
    allure_report = "allure generate {xml} -o {html}".format(xml=xml_report, html=html_report)
    logger.info(allure_report)
    os.popen(allure_report)
    logger.info("运行结束，生成测试报告♥❤！")


# python run_tests.py -m debug
@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
@click.option('-p', default=1, help='输入执行进程个数：Number ')
def run(m, p):
    if m is None or m == "run":
        for i in range(0, p):
            port = 4723 + 2 * i
            device_infos[i]["server_port"] = port
            device_infos[i]["system_port"] = port + 1

        with Pool(p) as pool:
            pool.map(run_pro, device_infos)
            pool.close()
            pool.join()

    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
