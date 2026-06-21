"""
==========================================================
MorphMotion AI
FPS Calculator
==========================================================
"""

import time
import cv2

from config import (
    SHOW_FPS,
    GREEN
)


class FPS:

    def __init__(self):

        self.previous_time = time.time()

        self.current_time = time.time()

        self.fps = 0

    def update(self):


        self.current_time = time.time()

        difference = self.current_time - self.previous_time

        if difference != 0:

            self.fps = 1 / difference

        self.previous_time = self.current_time

        return int(self.fps)

    def draw(self, frame):

        if not SHOW_FPS:
            return

        cv2.putText(
            frame,
            f"FPS : {int(self.fps)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            GREEN,
            2


        )