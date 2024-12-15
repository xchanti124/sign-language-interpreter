import threading

import matlab.engine

class SignClassifyThread:
    def __init__(self, matlab_path="./matlab"):
        self.lock = threading.Lock()
        self.engine = None
        self.running = True
        self.prediction = None

        self.thread = threading.Thread(target=self.start_matlab, args=(matlab_path,), daemon=True)
        self.thread.start()

    def start_matlab(self, matlab_path):
        # Start the MATLAB instance and initialize the neural network
        try:
            self.engine = matlab.engine.start_matlab()
            self.engine.addpath(matlab_path, nargout=0)
            self.engine.eval("persistent net; if isempty(net), load('./trained_network.mat', 'net'); end;", nargout=0)
        except Exception:
            print("Error starting MATLAB engine")

    def classify(self, landmarks):
        with self.lock:
            if not self.engine:
                return None

            try:
                # Avoid trying to classify images with incomplete or missing hand landmarks
                if len(landmarks) != 42:
                    return None

                landmarks_matlab = matlab.double(landmarks)
                self.prediction = self.engine.classifysign(landmarks_matlab)

                return self.prediction
            except Exception:
                print("Error during classification")
                return None

    def stop(self):
        self.running = False
        if self.engine:
            self.engine.quit()
        self.thread.join()
