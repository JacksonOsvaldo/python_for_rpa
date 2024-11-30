import pandas as pd


class ExcelManager:
    def read_excel(self, file_path: str) -> None:
        return pd.read_excel(file_path)
