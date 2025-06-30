# ui.py
import cv2
import time

prev_time = 0

def draw_ui(frame, score, blink_ratio, gaze_direction, distracted):
    global prev_time

    h, w, _ = frame.shape

    # Draw score bar background
    cv2.rectangle(frame, (30, 30), (230, 60), (50, 50, 50), -1)
    cv2.putText(frame, f"Score: {score}/10", (40, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Blink ratio
    cv2.putText(frame, f"Blink Ratio: {blink_ratio:.2f}", (w - 250, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    # Gaze direction
    cv2.putText(frame, f"Gaze: {gaze_direction}", (w - 250, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

    # Distraction warning
    if distracted:
        cv2.putText(frame, "⚠️ Not Focused!", (w // 2 - 80, h - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

    # FPS Counter
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time
    cv2.putText(frame, f"FPS: {int(fps)}", (30, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return frame