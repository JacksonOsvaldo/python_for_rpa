from selenium.webdriver.common.by import By

class IntranetLogin:
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    BTN_CLICK = (By.CLASS_NAME, 'btn.btn-primary')

class IntranetForm:
    pass