import pytest
import requests
import pandas as pd
# from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAutomation:
    @pytest.fixture(scope="class", autouse=True)
    def setup_browser(self):
        """Configura o WebDriver para os testes Selenium."""
        self.browser = webdriver.Chrome()
        yield
        self.browser.quit()

    @pytest.fixture
    def temp_dir(self, tmp_path):
        """Fornece um diretório temporário para arquivos de teste."""
        return tmp_path

    # Teste 1: Abrir uma página web com Selenium
    def test_open_page(self):
        url = "https://example.com"
        self.browser.get(url)
        assert "Example Domain" in self.browser.title

    # Teste 2: Fazer login em uma página web com Selenium
    def test_login(self):
        url = "https://example-login-page.com"
        self.browser.get(url)

        username_field = self.browser.find_element(By.NAME, "username")
        password_field = self.browser.find_element(By.NAME, "password")
        login_button = self.browser.find_element(By.ID, "login")

        username_field.send_keys("testuser")
        password_field.send_keys("password123")
        login_button.click()

        assert "Dashboard" in self.browser.page_source

    # Teste 3: Inserir valores em uma página web com Selenium
    def test_insert_values(self):
        url = "https://example-form.com"
        self.browser.get(url)

        input_field = self.browser.find_element(By.NAME, "input_field")
        submit_button = self.browser.find_element(By.NAME, "submit")

        input_field.send_keys("Test Value")
        submit_button.click()

        assert "Success" in self.browser.page_source

    # Teste 4: Baixar um arquivo via requests
    def test_download_file(self, temp_dir):
        url = "https://example.com/sample.xlsx"
        file_path = temp_dir / "sample.xlsx"

        response = requests.get(url)
        assert response.status_code == 200

        with open(file_path, "wb") as f:
            f.write(response.content)

        assert file_path.exists()

    # Teste 5: Leitura de arquivo baixado (xlsx) com Pandas
    def test_read_xlsx(self, temp_dir):
        xlsx_file = temp_dir / "sample.xlsx"

        # Cria um arquivo de exemplo
        data = {"Col1": [1, 2, 3], "Col2": ["A", "B", "C"]}
        df = pd.DataFrame(data)
        df.to_excel(xlsx_file, index=False)

        # Lê o arquivo criado
        read_df = pd.read_excel(xlsx_file)
        assert read_df.equals(df)

    # # Teste 6: Criação de PDF com FPDF
    # def test_create_pdf(self, temp_dir):
    #     pdf_file = temp_dir / "output.pdf"
        
    #     pdf = FPDF()
    #     pdf.add_page()
    #     pdf.set_font("Arial", size=12)
    #     pdf.cell(200, 10, txt="Hello World", ln=True, align="C")
    #     pdf.output(str(pdf_file))

    #     assert pdf_file.exists()
