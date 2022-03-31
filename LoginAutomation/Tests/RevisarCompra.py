from Tests.EscolherProduto import SelectProduct
from Config.config import Configuration
from selenium.webdriver.common.by import By

import time


class ReviewBy(SelectProduct):
    closeSell = '//*[@id="sc-buy-box-ptc-button"]/span'

    def __int__(self):
        self.driver.get(Configuration.driver)
        self.SelectProduct = SelectProduct

    '''Fechar Pedido'''
    Configuration.driver.find_element(By.XPATH, closeSell).click()
    time.sleep(2)

    '''Escolhendo endereço'''
    Configuration.driver.find_element(By.XPATH, '//*[@id="address-book-entry-0"]/div[2]/span').click()
    time.sleep(3)

    Configuration.driver.get("https://www.amazon.com.br/gp/buy/spc/handlers/display.html?hasWorkingJavascript=1")
    time.sleep(2)

    '''Obtendo tamanho da tela'''
    height = Configuration.driver.execute_script("return document.body.scrollHeight")

    '''Executando scroll na tela'''
    for cont in range(20):
        #executa o scroll
        Configuration.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        #compara o tamanho da página anterior com o novo scroll, se igual finaliza rolagem
        new_height = Configuration.driver.execute_script("return document.body.scrollHeight")
        if height == new_height:
            time.sleep(2)
        break
        #Se não, armazena novo valor do scroll
        height == new_height
        time.sleep(2)

    #Alterar um dos produtos
    Configuration.driver.find_element(By.XPATH, '//*[@id="spc-orders"]/div[3]/div/div[3]/div/div/div[2]/div['
                                                '1]/div/div[2]/div[3]/div/a').click()
    time.sleep(2)

    #Removendo product1
    Configuration.driver.find_element(By.XPATH, '//*[@id="spc-orders"]/div[3]/div/div[3]/div/div/div[2]/div['
                                                '1]/div/div[2]/div[3]/div/span[2]/a[2]').click()
    time.sleep(3)

    #Redirecionando ao topo da página
    Configuration.driver.execute_script("scroll(0, 0);")
    time.sleep(3)

    '''Retornar a home - atráves do link no footer da tela'''
    Configuration.driver.get("https://www.amazon.com.br/ref=ox_spc_footer_homepage")
    time.sleep(2)

    '''Realiznado checkout'''
    element = Configuration.driver.find_element(By.ID, 'nav-link-accountList')
    Configuration.action.move_to_element(element)
    Configuration.action.perform()
    time.sleep(3)
    Configuration.driver.find_element(By.XPATH, '//*[@id="nav-item-signout"]').click()
