from configs import PLANILHA, URL_INTRANET, LOGIN, SENHA
from services.get_planilha import GetPlanilha
from adapters.excel_manager import ExcelManager
from adapters.html_manager import HtmlManager
from pom.intranet import Intranet


class InsertValuesIntranet(Intranet):
    def __init__(self):
        super().__init__(URL_INTRANET)
        self.__login = LOGIN
        self.__password = SENHA
        self.__url_planilha = PLANILHA
        self.service_planilha = GetPlanilha()
        self.excel_manager = ExcelManager()
        self.html_manager = HtmlManager()

    def get_planilha(self):
        self.service_planilha.get_planilha(self.__url_planilha, "planilha.xlsx")

    def carrega_arquivo(self):
        return self.excel_manager.read_excel("planilha.xlsx")
    
    def insert_values_intranet(self):
        self.get_planilha()
        data = self.carrega_arquivo()
        self.login_intranet(self.__login, self.__password)
        if self.get_text() == self.__login:
            for index, value in data.iterrows():
                try:
                    self.post_values(value)
                except:
                    self.post_values(value)
            self.html_manager.html_to_pdf(self.get_html(), 'output.pdf')
            print('Dados preenchidos e PDF gerado')
        else:
            print('Login deu errado')