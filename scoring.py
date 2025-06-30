# scoring.py

def calculate_focus_score(blink_ratio, gaze_direction):
    # Ideal blink ratio range (approx)
    BLINK_THRESHOLD_LOW = 0.20
    BLINK_THRESHOLD_HIGH = 0.30

    # Blink score
    if blink_ratio < BLINK_THRESHOLD_LOW:
        blink_score = 0  # Eyes mostly closed
    elif blink_ratio > BLINK_THRESHOLD_HIGH:
        blink_score = 10  # Fully open
    else:
        blink_score = 5  # Normal blink

    # Gaze score
    if gaze_direction == "CENTER":
        gaze_score = 10
    else:
        gaze_score = 0

    # Final score
    score = int((blink_score + gaze_score) / 2)

    # Distraction logic
    distracted = True if score < 5 else False

    return score, distracted