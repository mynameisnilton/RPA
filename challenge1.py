import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Configuração do WebDriver
chromedriver_path = "H:\Elev Tecnologia\Scripts - Python\Desafio\chromedriver.exe"
service = Service(executable_path=chromedriver_path)
chrome_options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(service=service, options=chrome_options)

# Leitura do arquivo CSV
arquivo_lote = pd.read_csv('challenge(Sheet1).csv', encoding='ISO 8859-1')
js = arquivo_lote.to_json(orient='index')
obj = json.loads(js)


navegador.get('https://rpachallenge.com/')

#Clicar Start
navegador.find_element(By.CSS_SELECTOR, 'button[class="waves-effect col s12 m12 l12 btn-large uiColorButton"]').click()


i = -1
for atalho in obj:
    i += 1
    #Primeiro Nome
    atalho = obj[f'{i}']['First Name']
    print(atalho)
    sleep(3)
    navegador.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelFirstName"]').send_keys(atalho)
    sleep(3)

    #Sobrenome
    atalho = obj[f'{i}']['Last Name ']
    print(atalho)
    navegador.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelLastName"]').send_keys(atalho)
    sleep(3)

    #Nome Empresa
    atalho = obj[f'{i}']['Company Name']
    print(atalho)
    navegador.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelCompanyName"]').send_keys(atalho)
    sleep(3)

    #Cargo
    atalho = obj[f'{i}']['Role in Company']
    print(atalho)
    navegador.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelRole"]').send_keys(atalho)
    sleep(3)

    #Endereço
    atalho = obj[f'{i}']['Address']
    print(atalho)
    navegador.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelAddress"]').send_keys(atalho)
    sleep(3)

    #Email
    atalho = obj[f'{i}']['Email']
    print(atalho)
    navegador.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelEmail"]').send_keys(atalho)
    sleep(3)

    #Telefone
    atalho = obj[f'{i}']['Phone Number']
    print(atalho)
    navegador.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelPhone"]').send_keys(atalho)
    sleep(3)

    #Clicar Submit
    navegador.find_element(By.CSS_SELECTOR, 'input[value="Submit"]').click()

print('Fim do Programa')
