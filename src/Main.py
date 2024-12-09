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
        text = "Press a letter to start capturing landmarks"

    else:
        text = "Currently capturing landmarks for the letter " + chr(InputHandler.current_letter)

        image = processFrame(cap)
        cv2.putText(image, "Press BACKSPACE to choose another letter or ESC to exit", (50, 100),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, "Samples: " + str(count), (50, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)

    cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    ########################################################################################

    cv2.imshow("meow meow meow meow", image)

    if cv2.waitKey(1) & 0xFF == ESC_KEY:
        running = False

cap.release()
cv2.destroyAllWindows()
