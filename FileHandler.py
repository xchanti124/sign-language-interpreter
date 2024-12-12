import json
import csv

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json_data(self):
    try:
        self.coordinate_list = load_json('coordinate_data.json')
        self.label_list = load_json('label_data.json')
    except Exception:
        pass

def save_json_data(self):
    save_json('coordinate_data.json', self.coordinate_list)
    save_json('label_data.json', self.label_list)

def load_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data

def save_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def load_csv_data(self):
    try:
        self.coordinate_list = load_csv('coordinate_data.csv')
        self.label_list = load_csv('label_data.csv')
    except Exception:
        pass

def save_csv_data(self):
    save_csv('coordinate_data.csv', self.coordinate_list)
    save_csv('label_data.csv', self.label_list)

def save_data_loader(data_loader):
    save_csv('coordinate_data.csv', data_loader.coordinate_list)
    save_csv('label_data.csv', data_loader.label_list)