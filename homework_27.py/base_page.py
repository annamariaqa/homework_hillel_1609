from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilis.custom_conditions import WaitForNElements


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self.url = None


    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _present_element(self, locator, message='', timeout=1): 
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)
    
    def _input_field(self, locator, message='', timeout=1):  
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)
    
    def _present_text(self, locator, text, message='', timeout=1): 
        return WebDriverWait(self._driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text), message=message)
    
    def _button(self, locator, message='', timeout=1):  
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator), message=message)