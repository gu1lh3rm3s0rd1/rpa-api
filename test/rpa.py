# RPA
# selenium
# Desenvolva um RPA para acessar o Google e pesquise por Clima e extrair informações de clima e data.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# tratar caracter especial
import unicodedata
from datetime import datetime

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
driver.get('https://www.google.com.br')

# pesquisar por clima
pesquisa = driver.find_element(By.NAME, 'q')
pesquisa.send_keys('clima')
pesquisa.send_keys(Keys.RETURN)

# estrair informações de clima e data
clima = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="wob_tm"]'))).text
data = driver.find_element(By.XPATH, '//*[@id="wob_dts"]').text
dia, hora = data.split(',')
descricao = driver.find_element(By.XPATH, '//*[@id="wob_dc"]').text


grau = "C"
temperatura = f"{clima} {grau}"
temperatura = unicodedata.normalize('NFKD', temperatura).encode('ASCII', 'ignore').decode('ASCII')
dia = dia.strip()
hora = hora.strip()
data = datetime.now().strftime('%d/%m-%Y')
descricao = unicodedata.normalize('NFKD', descricao).encode('ASCII', 'ignore').decode('ASCII')

# print(temperatura)
# print(dia)
# print(hora)
# print(descricao)
# print(data)

driver.quit()
