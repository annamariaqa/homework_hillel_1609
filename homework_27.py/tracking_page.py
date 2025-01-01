from locators import TrackingPageLocators
from settings import url
from base_page import BasePage


class TrackingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = url
        self.locators = TrackingPageLocators()
    
    def tracking_number_input(self):
        return self._input_field(self.locators.input_track_number, message='Cant find tracking number input at Tracking Page',
                                 timeout=3)
    def _search_button(self):
        return self._button(self.locators.search_button, message='Cant find search button at Tracking Page', timeout=4)
    
    def _chat_button(self):
        return self._button(self.locators.chat_message_button , message='Cant find chat button at Tracking Page', timeout=4)
    
    def status_text(self):
        return self._present_element(self.locators.package_status)

    def set_tracking_number(self, track_number):
        self.tracking_number_input().send_keys(track_number)
        return self
    
    def click_search(self):
        self._search_button().click()
        return self
    
    def chat_button_click(self):
        self._chat_button().click()
        return self
    
    def check_status(self):
        status_element = self.status_text() 
        status_text = status_element.text  
        return status_text

    

