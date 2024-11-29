import cv2
from typing import Dict, List, Tuple
import string
from string import ascii_lowercase as alc


def is_key_pressed():
    key = cv2.pollKey()

    return key


def create_landmark_coordinate_dict():
    landmark_dict: Dict[string : List[Tuple]] = {}

    for letter in alc:
        landmark_dict[letter] = []

    return landmark_dict
