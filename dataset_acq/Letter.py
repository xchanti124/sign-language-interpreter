from dataset_acq import FileHandler

class Letter:

    coordinate_list = []
    label_list = []

    def __init__(self, letter: chr, landmarks):
        FileHandler.load_csv_data(self)
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
        FileHandler.save_csv_data(self)

