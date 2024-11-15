from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from adapters.web_manager import WebManager



class BasePage(WebManager):
    def __init__(self):
        super().__init__()
        self.__driver = self.get_webdriver()

    def find_element(self, *locator, timeout: float = 2):
        return WebDriverWait(self.__driver, timeout).until(EC.visibility_of_element_located(*locator))

    def find_elements(self, *locator):
        return self.__driver.find_elements(*locator)
    
    def send_keys(self, value: str, *locator):
        return self.find_element(*locator).send_keys(value)
    
    def click(self, *locator):
        return self.find_element(*locator).click()
    
    def select_by_value(self, value: str, *locator):
        return Select(self.find_element(*locator)).select_by_value(str(value))

    def open(self, url):
        self.__driver.get(url)

    def get_title(self):
        return self.__driver.title

    def get_url(self):
        return self.__driver.current_url
    

