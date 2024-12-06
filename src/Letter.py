import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

class Letter:

    coordinate_list = []
    label_list = []

    def __init__(self, letter: chr, landmarks):
        self.letter = chr(letter)
        self.landmarks = landmarks
        self.x = 0.0
        self.y = 0.0
        if self.letter not in self.dictionary:
            self.dictionary[self.letter] = []
        self.process()

    def process(self):
        landmark_map = {}
        for i in range(0, 21):
            hand_landmark_name = self.hand_landmark_names[i]
            self.x = self.landmarks.landmark[i].x
            self.y = self.landmarks.landmark[i].y
            landmark_map[hand_landmark_name] = {'x': self.x, 'y': self.y}

        self.dictionary[self.letter].append(landmark_map)
        save_json('data.json', self.dictionary)
