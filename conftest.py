import time
import allure
import pytest
from Common.driver import BaseDriver
from Utils.logger import logger
from allure_commons.types import AttachmentType

driver = None


def _capture_screenshot(driver):
    '''
    截图保存为png，展示到测试报告中
    :return:
    '''
    return driver.get_screenshot_as_png()


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例失败截图.
    :param item:
    """
    global driver
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            print(case_path)
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            screen_img = _capture_screenshot(driver)
            allure.attach(screen_img, name=case_name, attachment_type=AttachmentType.PNG)
        report.extra = extra

# 启动app
@pytest.fixture
def common_driver(cmdopt):
    global driver
    logger.info(cmdopt)
    base_driver = BaseDriver(eval(cmdopt))
    base_driver.start_appium()
    time.sleep(3)
    driver = base_driver.get_driver()
    yield driver
    # driver.close_app()
    driver.quit()



