import FileHandler

class DataLoader:
    def __init__(self):
        self.coordinate_list = []
        self.label_list = []

    def load_csv_data(self):
        try:
            self.coordinate_list = FileHandler.load_csv('coordinate_data.csv')
            self.label_list = FileHandler.load_csv('label_data.csv')
        except Exception:
            pass