
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


class Configuration:

    """Configuration driver"""
    chromeDriver = Service('../Config/chromedriver')
    driver = webdriver.Chrome(service=chromeDriver)
    driver.maximize_window()
    driver.get('https://www.amazon.com.br/ref=nav_logo')
    time.sleep(1)

    action = webdriver.ActionChains(driver)

    '''variáveis'''
    base_URL = "https://www.amazon.com.br/s?k={}&ref=nb_sb_noss"
    user_Name = "lffqa@outlook.com"
    password = "LFFQA24"
    login_url = ""
