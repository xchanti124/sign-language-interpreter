import time

import matlab.engine
import numpy as np
from sklearn.preprocessing import LabelEncoder

from src.DataLoader import DataLoader

def main():

    data_loader = DataLoader()
    data_loader.load_csv_data()

    trainData = np.array(data_loader.coordinate_list).astype(float)
    trainLabels = np.array(data_loader.label_list).ravel()


    label_encoder = LabelEncoder()
    trainLabels = label_encoder.fit_transform(trainLabels)

    engine = matlab.engine.start_matlab()
    engine.addpath("./matlab", nargout=0)

    trainData_matlab = matlab.double(trainData.tolist())
    trainLabels_matlab = matlab.double(trainLabels.tolist())

    engine.neuralnetwork(trainData_matlab, trainLabels_matlab, nargout=3)

    time.sleep(10000) #dont immediately quit
    engine.quit()


if __name__ == "__main__":
    main()
