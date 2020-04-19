import time
import pytest
from common.driver import base_driver

from page.objects.comm_page import CommonPage

driver = None

# 启动app
@pytest.fixture(scope='session', autouse=True)
def driver():
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



