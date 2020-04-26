import os
from time import sleep
import allure
from poium import PageElement, PageElements
from allure_commons.types import AttachmentType

from settings import REPORT_DIR
from Utils.handle_report import new_report_time
from Utils.logger import logger


def capture_screenshots(driver, file_name):
    """
    截图
    :param file_name: 截图名称
    :return:
    """
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", file_name)
    print("image_dir=", image_dir)
    driver.save_screenshot(image_dir)


class FindElement(PageElement):
    # 黑名单，用来处理一些不定时的弹框。
    black_list = []
    # 限制查找次数
    count = 0

    def get_element(self, context):
        try:
            elem = context.find_element(*self.locator)
        except:
            if self.count > 2:
                # logger.info("已经超过最大查找次数!")
                return None
            self.count += 1
            # 判断黑名单元素是否出现
            for black in self.black_list:
                black_elements = context.find_elements(*black)
                if len(black_elements) >= 1:
                    black_elements[0].click()
                    logger.info("黑名单{}元素出现，已点击!".format(black))

                else:
                    logger.info("黑名单{}元素未出现!".format(black))
            else:
                return self.get_element(context)

        else:
            try:
                style_red = 'arguments[0].style.border="2px solid red"'
                context.execute_script(style_red, elem)
            except BaseException:
                return elem
            return elem

    def find(self, context):

        for i in range(1, self.time_out):
            if self.log is False:
                logger.info("{desc}, {n} times search, {elm} ".format(desc=self.describe, n=i, elm=self.locator))
            if self.get_element(context) is not None:
                return self.get_element(context)
            else:
                sleep(1)
        else:
            if self.get_element(context) is None:
                file_name = '-'.join(self.locator) + "对象未找到截图.png"
                capture_screenshots(context, file_name)
                logger.info("{desc}, 对象未找到, {elm} ".format(desc=self.describe, elm=self.locator))
            return self.get_element(context)


class FindElements(PageElements):
    def find(self, context):
        if self.get_element(context) is not None:
            logger.info("{desc}, 对象已访问, {elm} ".format(desc=self.describe, elm=self.locator))
            try:
                return context.find_elements(*self.locator)
            except Exception:
                file_name = '-'.join(self.locator) + "对象未找到截图.png"
                capture_screenshots(context, file_name)
                # 日志
                logger.info("{desc}, 对象未找到, {elm} ".format(desc=self.describe, elm=self.locator))
                return []
        else:
            return []