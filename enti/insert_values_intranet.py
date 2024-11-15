from configs import PLANILHA, URL_INTRANET
from services.get_planilha import GetPlanilha
from adapters.excel_manager import ExcelManager
from adapters.web_manager import WebManager
from adapters.html_manager import HtmlManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from pom.intranet import Intranet


class InsertValuesIntranet(Intranet):
    def __init__(self):
        super().__init__(URL_INTRANET)
        self.__url_planilha = PLANILHA
        self.service_planilha = GetPlanilha()
        self.excel_manager = ExcelManager()
        self.html_manager = HtmlManager()

    def get_planilha(self):
        self.service_planilha.get_planilha(self.__url_planilha, "planilha.xlsx")

    def carrega_arquivo(self):
        return self.excel_manager.read_excel("planilha.xlsx")

    def post_values(self, driver, value):
        print(f"""Preenchendo valores: {value['First Name']} - {value['Last Name']} - {value['Sales Target']} - {value['Sales']}""")
        # driver.find_element(By.ID, 'firstname').send_keys(value['First Name'])
        # driver.find_element(By.ID, 'lastname').send_keys(value['Last Name'])
        # Select(driver.find_element(By.ID, 'salestarget')).select_by_value(str(value['Sales Target']))
        # driver.find_element(By.ID, 'salesresult').send_keys(value['Sales'])
        # try:
        #     driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        # except:
        #     driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    
    def insert_values_intranet(self):
        self.get_planilha()
        data = self.carrega_arquivo()
        self.login_intranet()
        # if self.driver.find_element(By.CLASS_NAME, 'username').text == self.login:
        #     for index, value in data.iterrows():
        #         try:
        #             self.post_values(self.driver, value)
        #         except:
        #             self.post_values(self.driver, value)
        #     self.html_manager.html_to_pdf(self.driver.find_element(By.ID, 'sales-results').get_attribute('innerHTML'), 'output.pdf')
        #     print('Dados preenchidos e PDF gerado')
        # else:
        #     print('Login deu errado')