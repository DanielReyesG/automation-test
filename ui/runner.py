from selenium import webdriver
from ui.base.shared_settings import SharedSettings
from ui.tests.tests import Test


class Runner:

    def set_driver_shared(self):
        driver = webdriver.Chrome('chromedriver');
        SharedSettings().set_driver(driver)


if __name__ == '__main__':
    obj = Runner()
    obj.set_driver_shared()
    test = Test().test1()
    test = Test().test2()
