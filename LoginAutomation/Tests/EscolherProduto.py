import time
from Tests.RealizarLogin import Login_Page
from Config.config import Configuration
from selenium.webdriver.common.by import By


class SelectProduct(Login_Page):

    product1 = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div'
    product2 = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div'
    product3 = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div'
    add = '//*[@id="add-to-cart-button"]'

    '''Çonstrutor da classe, executando página login'''
    def __init__(self):
        self.driver.get(Configuration.driver)
        self.Login_Page = Login_Page

    '''Método para construir url e buscar produto na página'''
    def get_url(buscarProduto):
        template = Configuration.base_URL
        buscarProduto = buscarProduto.replace(' ', '+')
        return template.format(buscarProduto)

    '''Adicionado três produtos ao carringo por meio da geração de url'''
    url = get_url('stabilo')
    Configuration.driver.get(url)
    time.sleep(1)
    Configuration.driver.find_element(By.XPATH, product1).click()
    Configuration.driver.find_element(By.XPATH, add).click()
    time.sleep(1)

    url2 = get_url('post it pacote')
    Configuration.driver.get(url2)
    time.sleep(1)
    Configuration.driver.find_element(By.XPATH, product2).click()
    Configuration.driver.find_element(By.XPATH, add).click()
    time.sleep(1)

    url3 = get_url('Python')
    Configuration.driver.get(url3)
    time.sleep(1)
    Configuration.driver.find_element(By.XPATH, product3).click()
    Configuration.driver.find_element(By.XPATH, add).click()
    time.sleep(2)

    '''Acessando carrinho'''
    Configuration.driver.find_element(By.XPATH, '//*[@id="sw-gtc"]/span').click()