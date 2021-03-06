from time import sleep
from poium import Page
from selenium.webdriver.support.wait import WebDriverWait
from Utils.logger import logger


class BasePage(Page):

    # 获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] * 0.9
                y1 = self.get_size()[1] / 2
                x2 = self.get_size()[0] / 10
                self.driver.swipe(x1, y1, x2, y1)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 向右滑动
    def swipe_right(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] / 10
                y1 = self.get_size()[1] / 2
                x2 = self.get_size()[0] * 0.9
                self.driver.swipe(x1, y1, x2, y1)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 向上滑动
    def swipe_up(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] / 2
                y1 = self.get_size()[1] * 0.9
                y2 = self.get_size()[1] / 10
                self.driver.swipe(x1, y1, x1, y2)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 向下滑动
    def swipe_down(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] / 2
                y1 = self.get_size()[1] / 10
                y2 = self.get_size()[1] * 0.9
                self.driver.swipe(x1, y1, x1, y2)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 滑动的方向
    def swipe_on(self, direction, count, time):
        try:
            if direction == 'up':
                self.swipe_up(count, time)
            elif direction == 'down':
                self.swipe_down(count, time)
            elif direction == 'right':
                self.swipe_right(count, time)
            else:
                self.swipe_left(count, time)
        except Exception as e:
            logger.info(e)

    def get_toast(self, str):
        message = "//*[contains(@text, '{}')]".format(str)
        print(message)
        try:
            # 获取toast提示框内容
            toast_element = WebDriverWait(self.driver, 5, 0.01).until(lambda x: x.find_element_by_xpath(message))
            return toast_element.text
        except:
            logger.exception("没有找到匹配的toast!!!")
            raise

