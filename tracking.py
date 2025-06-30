# tracking.py
import numpy as np
import mediapipe as mp

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
IRIS_LEFT = [468, 469, 470, 471]
IRIS_RIGHT = [473, 474, 475, 476]

def get_landmark_coordinates(landmarks, shape, indices):
    h, w = shape[:2]
    coords = [(int(landmarks.landmark[i].x * w), int(landmarks.landmark[i].y * h)) for i in indices]
    return coords

def get_blink_ratio(landmarks, shape):
    left_eye = get_landmark_coordinates(landmarks, shape, LEFT_EYE)
    right_eye = get_landmark_coordinates(landmarks, shape, RIGHT_EYE)

    def eye_ratio(eye):
        vertical = np.linalg.norm(np.array(eye[1]) - np.array(eye[5]))
        horizontal = np.linalg.norm(np.array(eye[0]) - np.array(eye[3]))
        return vertical / horizontal

    left_ratio = eye_ratio(left_eye)
    right_ratio = eye_ratio(right_eye)
    return (left_ratio + right_ratio) / 2

def get_gaze_direction(landmarks, shape):
    iris_left = get_landmark_coordinates(landmarks, shape, IRIS_LEFT)
    eye_left = get_landmark_coordinates(landmarks, shape, LEFT_EYE)

    iris_center = np.mean(iris_left, axis=0)
    eye_center = np.mean(eye_left, axis=0)

    dx = iris_center[0] - eye_center[0]

    if dx < -5:
        return "LEFT"
    elif dx > 5:
        return "RIGHT"
    else:
        return "CENTER"