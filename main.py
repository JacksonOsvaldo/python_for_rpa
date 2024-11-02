import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from weasyprint import HTML

PLANILHA = 'https://robotsparebinindustries.com/SalesData.xlsx'
URL_INTRANET = 'https://robotsparebinindustries.com'
LOGIN = 'maria'
SENHA = 'thoushallnotpass'

def baixa_planilha():
    response = requests.get(PLANILHA)
    if response.status_code == 200:
        open('planilha.xlsx', 'wb').write(response.content)

def carrega_dados_planilha():
    return pd.read_excel('planilha.xlsx')

def salva_resultado(tabela_html):
    HTML(string=tabela_html).write_pdf("output.pdf")

def operacoes_sistema():
    baixa_planilha()
    driver = webdriver.Chrome()
    driver.get(URL_INTRANET)
    driver.find_element(By.ID, 'username').send_keys(LOGIN)
    driver.find_element(By.ID, 'password').send_keys(SENHA)
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    time.sleep(5)
    if driver.find_element(By.CLASS_NAME, 'username').text == LOGIN:
        data = carrega_dados_planilha()
        for index, value in data.iterrows():
            driver.find_element(By.ID, 'firstname').send_keys(value['First Name'])
            driver.find_element(By.ID, 'lastname').send_keys(value['Last Name'])
            Select(driver.find_element(By.ID, 'salestarget')).select_by_value(str(value['Sales Target']))
            driver.find_element(By.ID, 'salesresult').send_keys(value['Sales'])
            try:
                driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
            except:
                time.sleep(2)
                driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        salva_resultado(driver.find_element(By.ID, 'sales-results').get_attribute('innerHTML'))
        print('Dados preenchidos')
    else:
        print('Login deu errado')

if __name__ == '__main__':
    operacoes_sistema()