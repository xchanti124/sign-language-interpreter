import cv2
from dataset_acq import InputHandler, FrameProcessor
from dataset_acq.InputHandler import updatedPressedKey
from dataset_acq.FrameProcessor import processFrame, getHandLandmarks
from dataset_acq.State import State
from dataset_acq.VideoCaptureThread import VideoCaptureThread

def main():
    cap = VideoCaptureThread(0)
    ESC_KEY = 27
    running = True

    while running:
        image = cap.read()
        if image is None:
            print("No frame captured")
            continue

        updatedPressedKey()

        # More processing before showing the image
        ########################################################################################
        results = FrameProcessor.hands.process(image)

        if InputHandler.current_state == State.SELECTING_LETTER:
            text = "Press a letter to start capturing landmarks"
            image = processFrame(image, False, results)

            getHandLandmarks(results)

        else:
            text = "Currently capturing landmarks for the letter " + chr(InputHandler.current_letter)

            image = processFrame(image, True, results)
            drawString(image, "Press BACKSPACE to choose another letter or ESC to exit", 50, 100)
            drawString(image, "Samples: " + str(InputHandler.count), 50, 150)
            InputHandler.count += 1
            if InputHandler.count == 1000:
                InputHandler.current_state = State.SELECTING_LETTER
                InputHandler.count = 0

        drawString(image, text, 50, 50)
        ########################################################################################

        cv2.imshow("mrreeeowwwww", image)

        if cv2.waitKey(1) & 0xFF == ESC_KEY:
            break

    cap.stop()
    cv2.destroyAllWindows()

def drawString(image, text, x, y):
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

if __name__ == "__main__":
    main()
