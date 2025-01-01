from selenium.webdriver.common.by import By

class TrackingPageLocators:
    input_track_number = (By.CLASS_NAME, 'track__form-group-input')
    search_button = (By.CLASS_NAME,'track__form-group-btn')
    chat_message_button = (By.XPATH, '//*[@id="chat"]/div[2]/button')
    package_status = (By.XPATH, '//*[@id="chat"]/header/div[2]/div[2]/div[2]')