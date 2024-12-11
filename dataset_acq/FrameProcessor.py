import mediapipe as mp
import cv2

from dataset_acq import InputHandler
from dataset_acq.Letter import Letter

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
        model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5
    )

# GBR
custom_landmark_style = mp_drawing.DrawingSpec(
    color=(0, 255, 0), thickness=2, circle_radius=2
)
custom_connection_style = mp_drawing.DrawingSpec(
    color=(255, 0, 0), thickness=2
)

def processFrame(cap, save_landmarks):
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        return None

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                custom_landmark_style,
                custom_connection_style,
            )

            if save_landmarks:
                Letter(InputHandler.current_letter, hand_landmarks)

    return image

def getHandLandmarks(cap):
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        return None

    results = hands.process(image)
    landmark_list = []

    if results.multi_hand_landmarks:

        for i in range(21):
            x = results.multi_hand_landmarks[0].landmark[i].x
            y = results.multi_hand_landmarks[0].landmark[i].y
            landmark_list.append(x)
            landmark_list.append(y)

    return landmark_list
