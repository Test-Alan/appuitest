import os
import time

import allure
import pytest
from common.driver import base_driver

from page.objects.comm_page import CommonPage
from allure_commons.types import AttachmentType

from settings import REPORT_DIR
from utils.handle_report import new_report_time

driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例失败截图.
    :param item:
    """
    global driver
    pytest_html = item.config.pluginmanager.getplugin('html')
    print(pytest_html)
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            screen_img = _capture_screenshot()
            allure.attach(screen_img, name=case_name, attachment_type=AttachmentType.PNG)
        report.extra = extra


def _capture_screenshot():
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    return driver.get_screenshot_as_png()

# 启动app
@pytest.fixture(scope='session', autouse=True)
def app():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    driver = base_driver()
    page = CommonPage(driver)
    page.skip_welcome_page()
    return driver


# 关闭app
@pytest.fixture(scope="session", autouse=True)
def driver_close():
    yield driver
    driver.quit()
    time.sleep(2)
    print("test end!")



