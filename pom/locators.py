from selenium.webdriver.common.by import By

class IntranetLogin:
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    USERNAME_LOGIN_PASS = (By.CLASS_NAME, 'username')
    BTN_CLICK = (By.CLASS_NAME, 'btn.btn-primary')

class IntranetForm:
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    SALES_TARGET = (By.ID, 'salestarget')
    SALES_RESULT = (By.ID, 'salesresult')
    BTN_CLICK = (By.CLASS_NAME, 'btn.btn-primary')
    RESULT_TABLE = (By.ID, 'sales-results')