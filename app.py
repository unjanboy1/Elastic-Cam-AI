import cv2
import pyautogui

from deformation.stretch_engine import StretchEngine
from ui.overlays import Overlays
from ui.effects import Effects
from recording.video_recorder import VideoRecorder

# Camera setup
cap = cv2.VideoCapture(0)

screen_w, screen_h = pyautogui.size()

# Modules
stretch = StretchEngine()
overlay = Overlays()
effects = Effects()
recorder = VideoRecorder(frame_size=(640, 480))

mode = "NORMAL"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Optional visual effect
    if mode == "NORMAL":
        frame = frame
    elif mode == "BLUR":
        frame = effects.blur(frame)
    elif mode == "HIGHLIGHT":
        frame = effects.highlight(frame)

    # UI text
    overlay.draw_text(frame, f"Mode: {mode} | Press Q to quit", (20, 40))

    # Recording
    recorder.write(frame)

    cv2.imshow("AI Deformation App", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('b'):
        mode = "BLUR"

    elif key == ord('h'):
        mode = "HIGHLIGHT"

    elif key == ord('n'):
        mode = "NORMAL"

# Cleanup
cap.release()
recorder.stop()
cv2.destroyAllWindows()