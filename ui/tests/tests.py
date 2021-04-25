from ui.base.shared_settings import SharedSettings
from ui.base.action import Actions
import time


class Test:
    btn_search = ("//button[contains(text(),'Search')]")
    btn_back = ("//a[@class ='btn btn-primary'][contains(text(),'Back')]")
    second_tarjet = ("//span[@class ='card-title'][contains(text(),'The Batman')]")
    txt_search = ("//input[@name='search']")
    url = ('/html/body/div/div[2]/div/div/div[2]/a')
    msj_imput_empty = ("//span[contains(text(),'Search cannot be empty.')]")
    card_content = ("//div[@class='card-content white-text']")

    def test1(self):
        driver = SharedSettings().get_driver()
        driver.get('http://localhost:3000/shows')
        button = driver.find_element_by_xpath(self.btn_search)
        button.click()
        if Actions.is_element_present(self.msj_imput_empty):
            print("Search cannot be empty.")
        if not Actions.is_element_present(self.card_content):
            print("Search without query not work well")
        search = driver.find_element_by_xpath(self.txt_search)
        search.send_keys("Test")
        button = driver.find_element_by_xpath(self.btn_search)
        button.click()
        if Actions.is_element_present(self.card_content):
            print("Successful test")
        else:
            print("Test Failed")

    def test2(self):
        driver = SharedSettings().get_driver()
        driver.get('http://localhost:3000/shows')
        Actions.is_element_present(self.btn_search)
        search = driver.find_element_by_xpath(self.txt_search)
        search.send_keys("Batman")
        button = driver.find_element_by_xpath(self.btn_search)
        button.click()
        driver.execute_script("window.scrollTo(0, window.scrollY + 600)")
        url = driver.find_element_by_xpath(self.url)
        url.click()
        driver.back()
        driver.execute_script("window.scrollTo(0, window.scrollY - 500)")
        time.sleep(5)
        back = driver.find_element_by_xpath(self.btn_back)
        back.click()
        input = driver.find_element_by_name("search")
        if input.text == '':
            print("Successful test")
        else:
            print("Test Failed")
        Actions.close_browser()
