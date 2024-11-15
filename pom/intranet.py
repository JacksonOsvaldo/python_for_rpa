from pom.base_page import BasePage
from pom.locators import IntranetLogin, IntranetForm
from configs import URL_INTRANET, LOGIN, SENHA

class Intranet(BasePage):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.__locator_login = IntranetLogin
        self.__locator_form = IntranetForm
        self.open(URL_INTRANET)

    def login_intranet(self):
        self.send_keys(LOGIN, self.__locator_login.USERNAME)
        self.send_keys(SENHA, self.__locator_login.PASSWORD)
        self.click(self.__locator_login.BTN_CLICK)