
from selenium.webdriver.common.by import By
from Config.config import Configuration
import time


class Login_Page:

    login_Button = '//*[@id="continue"]'
    password_Button = '//*[@id="signInSubmit"]'
    email = '//*[@id="ap_email"]'
    psw = '//*[@id="ap_password"]'
    connect = '//*[@id="authportal-main-section"]/div[2]/div/div/div/form/div/div[2]/div/div/label/div/label/input'

    """ Construtor da classe - Acessando site Amazon"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Configuration.driver)

    '''Realizando login'''
    Configuration.driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]').click()

    Configuration.driver.find_element(By.XPATH, login_Button).click()
    time.sleep(1)

    Configuration.driver.find_element(By.XPATH, email).send_keys(Configuration.user_Name)
    time.sleep(2)

    Configuration.driver.find_element(By.XPATH, login_Button).click()

    Configuration.driver.find_element(By.XPATH, psw).clear()
    time.sleep(1)

    Configuration.driver.find_element(By.XPATH, psw).send_keys(Configuration.password)
    time.sleep(1)

    Configuration.driver.find_element(By.XPATH, connect).click()
    time.sleep(2)

    Configuration.driver.find_element(By.XPATH, password_Button).click()
    time.sleep(2)


