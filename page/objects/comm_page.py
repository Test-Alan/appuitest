from common.base_page import BasePage
from common.element import FindElement
from page.locators.comm_locator import CommLocation as comm


class CommonPage(BasePage):
    welcome_title = FindElement(id_=comm.welcome_title_id, timeout=2)
    welcome_button = FindElement(id_=comm.welcome_button_id, timeout=2)

    # 跳过欢迎页
    def skip_welcome_page(self):
        if self.welcome_title:
            self.swipe_left(count=2)
            self.welcome_button.click()
