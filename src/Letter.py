import json
import numpy as np

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data(self):
    try:
        self.coordinate_list = load_json('coordinate_data.json')
        self.label_list = load_json('label_data.json')
    except Exception:
        pass

def save_data(self):
    save_json('coordinate_data.json', self.coordinate_list)
    save_json('label_data.json', self.label_list)

class Letter:

    coordinate_list = []
    label_list = []

    def __init__(self, letter: chr, landmarks):
        load_data(self)
        self.letter = chr(letter)
        self.landmarks = landmarks
        self.process()

    def process(self):
        self.label_list.append(self.letter)
        print(self.letter)
        landmark_list = []
        for i in range(21):
                x = self.landmarks.landmark[i].x
                y = self.landmarks.landmark[i].y
                landmark_list.append(x)
                landmark_list.append(y)

        self.coordinate_list.append(landmark_list)
        save_data(self)

