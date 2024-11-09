import requests

class GetPlanilha:
    def get_planilha(self, file_url: str, name_save_file: str) -> None:
        response = requests.get(file_url)
        if response.status_code == 200:
            open(name_save_file, 'wb').write(response.content)