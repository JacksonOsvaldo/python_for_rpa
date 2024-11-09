from selenium import webdriver

class WebManager:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument("--headless")
        
    def get_webdriver(self):
        return webdriver.Chrome(options=self.options)