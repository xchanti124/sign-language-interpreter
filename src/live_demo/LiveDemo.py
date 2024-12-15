import cv2

from src import FrameProcessor
from src.dataset_acq.InputHandler import updatedPressedKey
from src.FrameProcessor import getHandLandmarks, processFrameDrawSquare
from src.VideoCaptureThread import VideoCaptureThread
from src.live_demo.SignClassifyThread import SignClassifyThread

def main():

    cap = VideoCaptureThread(0)
    sign_classifier = SignClassifyThread()
    ESC_KEY = 27

    while True:
        image = cap.read()
        if image is None:
            print("No frame captured")
            continue

        updatedPressedKey() # idk why but if i remove this, mediapipe stutters

        ########################################################################################
        results = FrameProcessor.hands.process(image)
        prediction = str(sign_classifier.classify(getHandLandmarks(results)))
        image = processFrameDrawSquare(image, False, results, prediction)
        ########################################################################################

        cv2.imshow("Live Demo", image)

        if cv2.waitKey(1) & 0xFF == ESC_KEY:
            break

    cap.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

