from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager

import time
import pytest 

from locators import TrackingPageLocators
from tracking_page import TrackingPage
from settings import url, track_number


chrome_options = ChromiumOptions()
service = Service(ChromeDriverManager().install())

@pytest.fixture
def driver():
    chrome_options = ChromiumOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)
    time.sleep(2)
    yield driver
    driver.close()

@pytest.fixture
def tracking_page(driver):
    tracking_page = TrackingPage(driver)
    tracking_page.open_page()
    time.sleep(2)
    return tracking_page

def test_search_package(tracking_page,  expected_status="Отримана"):
    tracking_page.set_tracking_number(track_number).click_search()
    time.sleep(2)
    actual_status = tracking_page.chat_button_click().check_status()
    assert actual_status == expected_status
    time.sleep(2)



