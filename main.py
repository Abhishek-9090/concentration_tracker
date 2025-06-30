# main.py
from tracking import get_blink_ratio, get_gaze_direction
from scoring import calculate_focus_score
from ui import draw_ui
import cv2
import mediapipe as mp

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# OpenCV Video Capture
cap = cv2.VideoCapture(0)

blink_count = 0
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]
        blink_ratio = get_blink_ratio(landmarks, frame.shape)
        gaze_direction = get_gaze_direction(landmarks, frame.shape)

        score, distracted = calculate_focus_score(blink_ratio, gaze_direction)
        frame = draw_ui(frame, score, blink_ratio, gaze_direction, distracted)

    cv2.imshow("Real-time Concentration Tracker", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()