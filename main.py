from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Criando o executavel para emular o navegador sem precisar usar o arquivo do Webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Direciona para abrir o site 
driver.get("https://economia.uol.com.br/cotacoes/bolsas/")

input_busca = driver.find_element(By.ID, 'filled-normal')
input_busca.send_keys('PETR3.SA')
time.sleep(2)
input_busca.send_keys(Keys.ENTER)
time.sleep(2)

span_valor = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
valor = span_valor.text
print(f'Valor da contação da PETR3 é atualmente R${valor}')

# Para o navegador não fechar
input('')


 