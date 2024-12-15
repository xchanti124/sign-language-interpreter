import csv

def load_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data

def save_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

class DataLoader:
    def __init__(self):
        self.coordinate_list = []
        self.label_list = []

    def load_csv_data(self):
        try:
            self.coordinate_list = load_csv('./coordinate_data.csv')
            self.label_list = load_csv('./label_data.csv')
        except Exception:
            pass

    def save_csv_data(self):
        try:
            save_csv('./coordinate_data.csv', self.coordinate_list)
            save_csv('./label_data.csv', self.label_list)
        except Exception:
            pass

data_loader = DataLoader()
