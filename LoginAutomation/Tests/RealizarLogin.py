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

    # Acessar tela sem preencher e-mail
    Configuration.driver.find_element(By.XPATH, login_Button).click()
    time.sleep(1)

    # Login icorreto
    Configuration.driver.find_element(By.XPATH, email).clear()
    time.sleep(1)
    # Preencendo campo e-mail incorreto
    Configuration.driver.find_element(By.XPATH, email).send_keys("lffaq@outlook.com")
    time.sleep(4)
    Configuration.driver.find_element(By.XPATH, login_Button).click()

    '''Informando login correto'''
    # Limpando campo senha
    Configuration.driver.find_element(By.XPATH, email).clear()
    time.sleep(1)
    # Preencendo campo e-mail
    Configuration.driver.find_element(By.XPATH, email).send_keys(Configuration.user_Name)
    time.sleep(2)
    Configuration.driver.find_element(By.XPATH, login_Button).click()

    '''Informando senha icorreta'''
    # Limpando campo senha
    Configuration.driver.find_element(By.XPATH, psw).clear()
    time.sleep(1)
    # Preenchendo campo senha
    Configuration.driver.find_element(By.XPATH, psw).send_keys("senhaErrada")
    time.sleep(1)
    # Logando
    Configuration.driver.find_element(By.XPATH, password_Button).click()
    time.sleep(4)

    '''Informando senha correta'''
    # Limpando campo senha
    Configuration.driver.find_element(By.XPATH, psw).clear()
    time.sleep(1)
    # Preenchendo campo senha
    Configuration.driver.find_element(By.XPATH, psw).send_keys(Configuration.password)
    time.sleep(1)
    # Marcando campo Mantenha-me conectado
    Configuration.driver.find_element(By.XPATH, connect).click()
    time.sleep(2)
    # Logando
    Configuration.driver.find_element(By.XPATH, password_Button).click()
    time.sleep(2)
