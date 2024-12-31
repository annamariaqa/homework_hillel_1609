from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time


chrome_options = ChromiumOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get("http://localhost:8000/dz.html")


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1) 

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)  

driver.switch_to.frame(driver.find_element(By.ID, "frame2"))

for _ in range(1):
    input = driver.find_element(By.ID, "input2")
    input.send_keys("Frame2_Secret")
    frame1_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
    frame1_button.click()
    alert = Alert(driver)
    print("Верифікація пройшла успішно!", alert.text)
    alert.accept()
    time.sleep(1) 


driver.quit()