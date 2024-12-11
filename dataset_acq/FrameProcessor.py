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

def processFrame(image, save_landmarks, results):

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

def getHandLandmarks(results):
    landmark_list = []

    if results.multi_hand_landmarks:

        for i in range(21):
            x = results.multi_hand_landmarks[0].landmark[i].x
            y = results.multi_hand_landmarks[0].landmark[i].y
            landmark_list.append(x)
            landmark_list.append(y)

