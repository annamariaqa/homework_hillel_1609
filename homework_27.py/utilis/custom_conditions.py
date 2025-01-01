from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WaitForNElements:
    def __init__(self, locator, quantity):
        self.locator = locator
        self.quantity = quantity

    def __call__(self, driver):
        try:
            print(f'Wait for element {self.locator[1]}')
            elements = driver.find_elements(*self.locator) 
            return len(elements) == self.quantity  
        except:
            return False  