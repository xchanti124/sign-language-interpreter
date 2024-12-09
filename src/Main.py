import cv2

from src import InputHandler
from src.InputHandler import updated_pressed_key
from src.FrameProcessor import processFrame
from src.State import State

ESC_KEY = 27
running = True

cap = cv2.VideoCapture(0)

while running:
    success, image = cap.read()

    if not success:
        print("Failed to grab frame")
        continue

    updated_pressed_key()

    # More processing before showing the image
    ########################################################################################
    if InputHandler.current_state == State.SELECTING_LETTER:
        pass
    else:
        image = processFrame(cap)

    ########################################################################################

    cv2.imshow("meow meow meow meow", image)

    if cv2.waitKey(1) & 0xFF == ESC_KEY:
        running = False

cap.release()
cv2.destroyAllWindows()
