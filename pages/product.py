from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class ProductPage:

    def __init__(self, driver):
        self.driver = driver


    def check_titlt_is(self, title):
        title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'btn btn-success btn')]")))
        title.click()
        popup = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        popup_text = popup.text
        popup.accept()
        assert popup_text == 'Product added'

    def chech_count(self, n):
        proverka = WebDriverWait(self.driver, 10).until(EC.url_contains('#'))
        monitor = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='card-block']")))
        assert len(monitor) == n