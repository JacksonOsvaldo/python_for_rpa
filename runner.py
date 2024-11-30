from enti.insert_values_intranet import InsertValuesIntranet
from adapters.os_manager import OsManager


class Runner:
    def __init__(self):
        self.insert_values = InsertValuesIntranet()
        OsManager.create_temp_folder()

    def intranet_values(self):
        self.insert_values.insert_values_intranet()
