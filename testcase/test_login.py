from page.objects.login_page import LoginPage
import pytest
import time


class TestLogin:

    def setup(self):
        print(111111)

    def teardown(self):
        print(22222)

    def test_login_succeed(self, driver):
        page = LoginPage(driver)
        page.phone_input = "13912345678"
        page.ver_code_but.click()
        page.ver_code_input = "0000"
        page.login_but.click()

        msg = page.get_toast("短信验证码校验不通过!")
        print(msg)
        assert msg == "短信验证码校验不通过!"
        time.sleep(20)

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])