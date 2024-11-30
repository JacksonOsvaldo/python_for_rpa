from configs import PLANILHA, URL_INTRANET, LOGIN, SENHA
from services.get_planilha import GetPlanilha
from adapters.excel_manager import ExcelManager
from adapters.html_manager import HtmlManager
from pom.intranet import Intranet
from configs import log


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
        log.info(__name__, "Iniciando baixa de planilha.")
        self.service_planilha.get_planilha(self.__url_planilha, "temp/planilha.xlsx")
        log.info(__name__, "Planilha baixada com sucesso.")

    def carrega_arquivo(self):
        log.info(__name__, "Carregando dados da planilha")
        return self.excel_manager.read_excel("temp/planilha.xlsx")

    def insert_values_intranet(self):
        self.get_planilha()
        data = self.carrega_arquivo()
        log.info(__name__, "Iniciando loging na intranet")
        self.login_intranet(self.__login, self.__password)
        if self.get_text() == self.__login:
            log.info(__name__, "Login bem sucedido. Iniciando operação.")
            for index, value in data.iterrows():
                log.info(
                    __name__,
                    f"""Preenchendo valores: {value['First Name']} - {value['Last Name']} - {value['Sales Target']} - {value['Sales']}""",
                )
                try:
                    self.post_values(value)
                except:
                    log.warning(
                        __name__,
                        "Preenchimento com erro. Realizando segunda tentativa.",
                    )
                    self.post_values(value)
            self.html_manager.html_to_pdf(self.get_html(), "temp/output.pdf")
            log.info(__name__, "Dados preenchidos e PDF gerado")
        else:
            log.error(__name__, "Login deu errado.")
