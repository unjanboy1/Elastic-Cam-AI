import cv2
import pyautogui

from tracking.hand_tracker import HandTracker
from deformation.stretch_engine import StretchEngine
from ui.overlays import Overlays

cap = cv2.VideoCapture(0)

tracker = HandTracker()
stretch = StretchEngine()
overlay = Overlays()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    hands = tracker.find_hands(frame)

    if hands:
        lmList = hands[0]

        # index finger tip (ID 8)
        x, y = lmList[8][1], lmList[8][2]

        points = [
            (x, y),
            (x + 50, y + 50),
            (x + 100, y),
            (x - 50, y + 50)
        ]

        stretched = stretch.apply_stretch(frame, points, (x, y))

        for px, py in stretched:
            cv2.circle(frame, (px, py), 10, (0, 255, 0), -1)

    overlay.draw_text(frame, "REAL HAND TRACKING ACTIVE", (20, 40))

    cv2.imshow("ElasticCam AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()