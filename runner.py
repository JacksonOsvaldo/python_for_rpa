from enti.insert_values_intranet import InsertValuesIntranet

class Runner:
    def __init__(self):
        self.insert_values = InsertValuesIntranet()

    def intranet_values(self):
        self.insert_values.insert_values_intranet()