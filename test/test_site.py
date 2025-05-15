
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.homepage import HomePage
from pages.product import ProductPage




def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_titlt_is()
    

def test_open_s5(driver):
    homepage = HomePage(driver)
    homepage.open()
    driver.get('https://www.demoblaze.com/index.html')
    homepage.click_monitor()
    product_page = ProductPage(driver)
    product_page.chech_count(2)
