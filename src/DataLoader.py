from src import FileHandler
from src.FileHandler import save_csv


class DataLoader:
    def __init__(self):
        self.coordinate_list = []
        self.label_list = []

    def load_csv_data(self):
        try:
            self.coordinate_list = FileHandler.load_csv('./coordinate_data.csv')
            self.label_list = FileHandler.load_csv('./label_data.csv')
        except Exception:
            pass

    def save_csv_data(self):
        try:
            save_csv('./coordinate_data.csv', self.coordinate_list)
            save_csv('./label_data.csv', self.label_list)
        except Exception:
            pass

data_loader = DataLoader()
