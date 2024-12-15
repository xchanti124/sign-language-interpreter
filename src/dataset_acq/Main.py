import cv2

from src.DataLoader import data_loader
from src.dataset_acq import InputHandler
from src import FrameProcessor
from src.dataset_acq.InputHandler import updatedPressedKey
from src.FrameProcessor import processFrame
from src.dataset_acq.State import State
from src.VideoCaptureThread import VideoCaptureThread

def main():
    data_loader.load_csv_data()

    cap = VideoCaptureThread(0)
    ESC_KEY = 27

    while True:
        image = cap.read()
        if image is None:
            print("No frame captured")
            continue

        updatedPressedKey()

        ########################################################################################
        results = FrameProcessor.hands.process(image)

        if InputHandler.current_state == State.SELECTING_LETTER:
            text = "Press a letter to start capturing landmarks"
            image = processFrame(image, False, results)

        else:
            text = "Currently capturing landmarks for the letter " + chr(InputHandler.current_letter)
            image = processFrame(image, True, results)

            drawString(image, "Press BACKSPACE to choose another letter or ESC to exit", 50, 100)
            drawString(image, "Samples: " + str(InputHandler.count), 50, 150)

            InputHandler.count += 1
            if InputHandler.count == 500:
                InputHandler.current_state = State.SELECTING_LETTER
                InputHandler.count = 0

        drawString(image, text, 50, 50)
        ########################################################################################

        cv2.imshow("dataset acq", image)

        if cv2.waitKey(1) & 0xFF == ESC_KEY:
            break

    data_loader.save_csv_data()
    cap.stop()
    cv2.destroyAllWindows()

def drawString(image, text, x, y):
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

if __name__ == "__main__":
    main()
