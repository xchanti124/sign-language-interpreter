from src.DataLoader import data_loader

class Letter:

    def __init__(self, letter: chr, landmarks):
        self.letter = chr(letter)
        self.landmarks = landmarks
        self.process()

    def process(self):
        data_loader.label_list.append(self.letter)
        print(self.letter)
        landmark_list = []
        for i in range(21):
                x = self.landmarks.landmark[i].x
                y = self.landmarks.landmark[i].y
                landmark_list.append(x)
                landmark_list.append(y)

        data_loader.coordinate_list.append(landmark_list)
