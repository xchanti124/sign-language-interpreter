import cv2

from dataset_acq import InputHandler
from dataset_acq.InputHandler import updated_pressed_key
from dataset_acq.FrameProcessor import processFrame
from dataset_acq.State import State

ESC_KEY = 27
running = True
count = 0

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
        image = processFrame(cap, False)

    else:
        text = "Currently capturing landmarks for the letter " + chr(InputHandler.current_letter)

        image = processFrame(cap, True)
        cv2.putText(image, "Press BACKSPACE to choose another letter or ESC to exit", (50, 100),  cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, "Samples: " + str(count), (50, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2,  cv2.LINE_AA)
        count += 1
        if count == 1000:
            InputHandler.current_state = State.SELECTING_LETTER
            count = 0

    cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    ########################################################################################

    cv2.imshow("meow meow meow meow", image)

    if cv2.waitKey(1) & 0xFF == ESC_KEY:
        running = False

cap.release()
cv2.destroyAllWindows()