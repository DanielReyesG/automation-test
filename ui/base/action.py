from ..base.shared_settings import SharedSettings
from selenium.webdriver.support.wait import WebDriverWait


class Actions:

    def is_element_present(element_to_find):
        driver = SharedSettings.get_driver()
        try:
            search = driver.find_element_by_xpath(element_to_find)
            wait = WebDriverWait(driver, timeout=30)
            if search is not None:
                return True
            else:
                print(f"Element is not present: {element_to_find}")
                return False
        except Exception:
            return False

    @staticmethod
    def close_browser():
        driver = SharedSettings.get_driver()
        driver.quit()
