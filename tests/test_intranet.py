import pytest
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from weasyprint import HTML


class TestAutomation:

    @pytest.fixture
    def temp_dir(self, tmp_path):
        """Fornece um diretório temporário para arquivos de teste."""
        return tmp_path

    def test_download_file(self, temp_dir):
        file_path = temp_dir / "SalesData.xlsx"

        response = requests.get("https://robotsparebinindustries.com/SalesData.xlsx")

        if response.status_code == 200:
            open(file_path, "wb").write(response.content)

        assert response.status_code == 200
        assert file_path.exists()

    def test_load_xlsx(self, temp_dir):
        file_path = temp_dir / "SalesData.xlsx"

        response = requests.get("https://robotsparebinindustries.com/SalesData.xlsx")

        if response.status_code == 200:
            open(file_path, "wb").write(response.content)

        read_df = pd.read_excel(file_path)
        assert read_df.empty == False

    def test_open_intranet(self):
        browser = webdriver.Chrome()
        url = "https://robotsparebinindustries.com"
        browser.get(url)
        assert "RobotSpareBin Industries Inc. - Intranet" in browser.title

    def test_login(self):
        browser = webdriver.Chrome()
        url = "https://robotsparebinindustries.com"
        browser.get(url)
        browser.find_element(By.ID, "username").send_keys("maria")
        browser.find_element(By.ID, "password").send_keys("thoushallnotpass")
        browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
        time.sleep(4)
        text = browser.find_element(By.CLASS_NAME, "username").text
        assert "maria" == text

    def test_insert_value(self):
        browser = webdriver.Chrome()
        url = "https://robotsparebinindustries.com"
        browser.get(url)

        # Login
        browser.find_element(By.ID, "username").send_keys("maria")
        browser.find_element(By.ID, "password").send_keys("thoushallnotpass")
        browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
        time.sleep(4)

        # Inserção valores
        browser.find_element(By.ID, "firstname").send_keys("Teste")
        browser.find_element(By.ID, "lastname").send_keys("Teste")
        Select(browser.find_element(By.ID, "salestarget")).select_by_value("30000")
        browser.find_element(By.ID, "salesresult").send_keys("5000")
        browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

        time.sleep(4)
        text = browser.find_element(
            By.XPATH, '//*[@id="sales-results"]/table/tbody/tr/td[1]'
        ).text

        assert "Teste" in text

    def test_print_table(self, temp_dir):
        file_path = temp_dir / "result.pdf"

        browser = webdriver.Chrome()
        url = "https://robotsparebinindustries.com"
        browser.get(url)

        # Login
        browser.find_element(By.ID, "username").send_keys("maria")
        browser.find_element(By.ID, "password").send_keys("thoushallnotpass")
        browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
        time.sleep(4)

        # Inserção valores
        browser.find_element(By.ID, "firstname").send_keys("Teste")
        browser.find_element(By.ID, "lastname").send_keys("Teste")
        Select(browser.find_element(By.ID, "salestarget")).select_by_value("30000")
        browser.find_element(By.ID, "salesresult").send_keys("5000")
        browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

        time.sleep(4)
        source_html = browser.find_element(By.ID, "sales-results").get_attribute(
            "innerHTML"
        )
        HTML(string=source_html).write_pdf(file_path)

        assert file_path.exists()
