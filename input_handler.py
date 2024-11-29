import cv2


def is_key_pressed():
    key = cv2.pollKey()

    return key
