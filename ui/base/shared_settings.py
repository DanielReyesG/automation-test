from unittest.util import safe_repr


class AppSettings:
    def __init__(self, driver=""):
        self.driver = driver


app_settings = AppSettings()


class SharedSettings:

    @staticmethod
    def set_driver(driver):
        global app_settings
        app_settings.driver = driver

    @staticmethod
    def get_driver():
        return app_settings.driver

    def assertFalse(self, expr, msg=None):
        if expr:
            msg = self._formatMessage(msg, "%s is not false" % safe_repr(expr))
            raise self.failureException(msg)
            return False
        else:
            return True
