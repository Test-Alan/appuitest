from common.base_page import BasePage
from common.element import FindElement
from page.locators.login_locator import LoginLocation as login


class LoginPage(BasePage):
    phone_input = FindElement(id_=login.phone_id, describe="手机号输入框")
    ver_code_but = FindElement(id_=login.ver_code_id, describe="获取验证码")
    ver_code_input = FindElement(id_=login.check_id, describe="验证码输入框")
    login_but = FindElement(id_=login.login_id, describe="登录按钮")
