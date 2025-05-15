from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class HomePage:
    def __init__(self, driver):
        self.driver = driver



    def open(self):
        self.driver.get('https://www.demoblaze.com/index.html')

    
    def click_galaxy_s6(self):
        galaxy_s6 = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Samsung galaxy s6']")))
        galaxy_s6.click()

    
    def click_monitor(self):
        monitors = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '''//*[@onclick="byCat('monitor')"]''')))
        monitors.click()