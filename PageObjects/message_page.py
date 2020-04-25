from Common.base_page import BasePage
from Common.element import FindElement

class MessagePage(BasePage):
    tz = FindElement(xpath='//androidx.appcompat.app.ActionBar.c[@content-desc="通知"]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')