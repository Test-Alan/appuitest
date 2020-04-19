from utils.handle_yaml import read_yaml
from settings import CAPS_DIR
from appium import webdriver


def base_driver(port=4723, **kwargs):
    caps = read_yaml(CAPS_DIR)
    if kwargs:
        k, v = next(iter(kwargs.items()))
        caps[k] = v
    print(caps)
    driver = webdriver.Remote("http://localhost:{}/wd/hub".format(port), caps)
    # driver.implicitly_wait(5)
    return driver