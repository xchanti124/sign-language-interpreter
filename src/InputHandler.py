import cv2

from src.State import State

current_letter = None
current_state = State.SELECTING_LETTER

def updated_pressed_key():
    global current_letter, current_state
    key = cv2.pollKey()
    if 97 <= key <= 122:
        current_letter = key
        current_state = State.CAPTURING_LANDMARKS
    elif key == 127:
        current_letter = None
        current_state = State.SELECTING_LETTER

