import time
from configs import PLANILHA, LOGIN, SENHA, URL_INTRANET
from services.get_planilha import GetPlanilha
from adapters.excel_manager import ExcelManager
from adapters.web_manager import WebManager
from adapters.html_manager import HtmlManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class InsertValuesIntranet:
    def __init__(self):
        self.url_planilha = PLANILHA
        self.login = LOGIN
        self.senha = SENHA
        self.url_intranet = URL_INTRANET
        self.service_planilha = GetPlanilha()
        self.excel_manager = ExcelManager()
        self.web_manager = WebManager()
        self.html_manager = HtmlManager()

    def get_planilha(self):
        self.service_planilha.get_planilha(self.url_planilha, "planilha.xlsx")

    def carrega_arquivo(self):
        return self.excel_manager.read_excel("planilha.xlsx")
    
    def post_values(self, driver, value):
        print(f"""Preenchendo valores: {value['First Name']} - {value['Last Name']} - {value['Sales Target']} - {value['Sales']}""")
        driver.find_element(By.ID, 'firstname').send_keys(value['First Name'])
        
        driver.find_element(By.ID, 'lastname').send_keys(value['Last Name'])
        
        Select(driver.find_element(By.ID, 'salestarget')).select_by_value(str(value['Sales Target']))
        
        driver.find_element(By.ID, 'salesresult').send_keys(value['Sales'])
        try:
            driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        except:
            driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    
    def insert_values_intranet(self):
        self.get_planilha()
        data = self.carrega_arquivo()
        driver = self.web_manager.get_webdriver()

        driver.get(URL_INTRANET)
        driver.find_element(By.ID, 'username').send_keys(self.login)
        driver.find_element(By.ID, 'password').send_keys(self.senha)
        driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        time.sleep(5)
        if driver.find_element(By.CLASS_NAME, 'username').text == self.login:
            for index, value in data.iterrows():
                try:
                    self.post_values(driver, value)
                except:
                    self.post_values(driver, value)
            self.html_manager.html_to_pdf(driver.find_element(By.ID, 'sales-results').get_attribute('innerHTML'), 'output.pdf')
            print('Dados preenchidos')
        else:
            print('Login deu errado')