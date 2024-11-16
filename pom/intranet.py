from pom.base_page import BasePage
from pom.locators import IntranetLogin, IntranetForm

class Intranet(BasePage):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.__locator_login = IntranetLogin
        self.__locator_form = IntranetForm
        self.open(url)

    def login_intranet(self, login: str, password: str):
        self.send_keys(login, self.__locator_login.USERNAME)
        self.send_keys(password, self.__locator_login.PASSWORD)
        self.click(self.__locator_login.BTN_CLICK)
    
    def get_text(self) -> None:
        return self.text(self.__locator_login.USERNAME_LOGIN_PASS)
    
    def post_values(self, value: dict):
        print(f"""Preenchendo valores: {value['First Name']} - {value['Last Name']} - {value['Sales Target']} - {value['Sales']}""")
        self.send_keys(value['First Name'], self.__locator_form.FIRST_NAME)
        self.send_keys(value['Last Name'], self.__locator_form.LAST_NAME)
        self.select_by_value(value['Sales Target'], self.__locator_form.SALES_TARGET)
        self.send_keys(value['Sales'], self.__locator_form.SALES_RESULT)
        self.click(self.__locator_form.BTN_CLICK)

    def get_html(self) -> None:
        return self.html(self.__locator_form.RESULT_TABLE)