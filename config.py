"""
===========================================================
MorphMotion AI
Configuration File
-----------------------------------------------------------
Contains all project-wide constants and settings.
===========================================================
"""

# ==========================
# Camera Settings
# ==========================

CAMERA_INDEX = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

FPS = 30

# ==========================
# Window Settings
# ==========================

WINDOW_NAME = "MorphMotion AI"

FULLSCREEN = False

# ==========================
# MediaPipe Detection
# ==========================

HAND_DETECTION_CONFIDENCE = 0.7
HAND_TRACKING_CONFIDENCE = 0.7

POSE_DETECTION_CONFIDENCE = 0.7
POSE_TRACKING_CONFIDENCE = 0.7

FACE_DETECTION_CONFIDENCE = 0.7
FACE_TRACKING_CONFIDENCE = 0.7

# ==========================
# Gesture Settings
# ==========================

# Distance (pixels) between thumb and index
# below which a pinch is detected.

PINCH_THRESHOLD = 30

# Minimum frames before confirming grab
GRAB_CONFIRMATION_FRAMES = 4

# ==========================
# Stretch Settings
# ==========================

MAX_STRETCH_DISTANCE = 350

RUBBER_RETURN_SPEED = 0.15

RUBBER_ELASTICITY = 0.90

# ==========================
# Drawing Colors (BGR)
# ==========================

GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
CYAN = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ==========================
# Landmark Drawing
# ==========================

LANDMARK_RADIUS = 4

LINE_THICKNESS = 2

FONT_SCALE = 0.7

TEXT_THICKNESS = 2

# ==========================
# Keyboard Controls
# ==========================

KEY_EXIT = 27          # ESC

KEY_RECORD = ord('r')

KEY_SCREENSHOT = ord('s')

KEY_CLEAR = ord('c')

KEY_RESET = ord('x')

# ==========================
# Recording
# ==========================

OUTPUT_FOLDER = "output"

VIDEO_CODEC = "mp4v"

VIDEO_EXTENSION = ".mp4"

# ==========================
# Debug
# ==========================

SHOW_HAND_LANDMARKS = True

SHOW_POSE_LANDMARKS = True

SHOW_FACE_LANDMARKS = False

SHOW_FPS = True


SHOW_GRAB_POINT = True

SHOW_DEBUG_TEXT = True