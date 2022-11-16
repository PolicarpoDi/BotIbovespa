from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# função para remover o modo grafico do Selenium
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pandas as pd


def coleta_dados():
    options = Options()
    options.add_argument('--headless')

    # Criando o executavel para emular o navegador sem precisar usar o arquivo do Webdriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Direciona para abrir o site 
    driver.get("https://economia.uol.com.br/cotacoes/bolsas/")

    lista_acoes = ['B3SA3', 'KLBN4', 'ABEV3', 'BBAS3', 'EGIE3', 'ITSA4', 'PETR3', 'PETR4', 'VALE3', 'TAEE11', 'WEGE3', 'EMBR3']
    lista_valor = list()
    lista_dt = list()

    for acao in lista_acoes:
        input_busca = driver.find_element(By.ID, 'filled-normal')
        input_busca.send_keys(acao)
        time.sleep(2)
        input_busca.send_keys(Keys.ENTER)
        time.sleep(2)
        span_valor = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
        valor = span_valor.text
        
        lista_valor.append(valor)
        lista_dt.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        print(f'Empresa: {acao} cotação atual R${valor}.')
        
    dados = {
        'empresas': lista_acoes,
        'valor': lista_valor,
        'data_hora': lista_dt,
    }
    
    return dados

def gera_excel(dados, filename):
    df_acoes = pd.DataFrame(dados)
    # Instalar o pacote openpyxl para manipulação de xls e xlsx
    # para remover o indice, informe False no index
    df_acoes.to_excel(filename, index=False)


# Para o navegador não fechar
# input('')

dados = coleta_dados()
gera_excel(dados, './empresas_acoes.xlsx')


 