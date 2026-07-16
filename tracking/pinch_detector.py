"""
==========================================================
MorphMotion AI
Pinch Detection Module
----------------------------------------------------------
Detects pinch gesture using thumb and index finger.


Input:
    Hand landmarks from HandTracker

Output:
    - Pinch detected or not
    - Pinch distance
    - Pinch center
==========================================================
"""

import math

from config import (
    PINCH_THRESHOLD,
    GRAB_CONFIRMATION_FRAMES
)


class PinchDetector:

    def __init__(self):

        self.pinch_counter = 0
        self.is_grabbing = False

    # -------------------------------------------------
    # Euclidean Distance
    # -------------------------------------------------

    @staticmethod
    def distance(p1, p2):

        return math.hypot(
            p2[0] - p1[0],
            p2[1] - p1[1]
        )

    # -------------------------------------------------
    # Mid Point
    # -------------------------------------------------

    @staticmethod
    def midpoint(p1, p2):

        return (
            (p1[0] + p2[0]) // 2,
            (p1[1] + p2[1]) // 2
        )

    # -------------------------------------------------
    # Detect Pinch
    # -------------------------------------------------

    def detect(self, hand_landmarks):

        """
        hand_landmarks format:

        [
            [id,x,y],
            [id,x,y],
            ...
        ]
        """

        if len(hand_landmarks) != 21:

            self.reset()

            return {
                "pinching": False,
                "grabbed": False,
                "distance": None,
                "center": None
            }

        thumb = hand_landmarks[4][1:]
        index = hand_landmarks[8][1:]

        dist = self.distance(thumb, index)

        center = self.midpoint(thumb, index)

        pinching = dist < PINCH_THRESHOLD

        # -------------------------------
        # Stabilize gesture
        # -------------------------------

        if pinching:

            self.pinch_counter += 1

        else:

            self.pinch_counter = 0
            self.is_grabbing = False

        if self.pinch_counter >= GRAB_CONFIRMATION_FRAMES:

            self.is_grabbing = True

        return {

            "pinching": pinching,

            "grabbed": self.is_grabbing,

            "distance": dist,

            "center": center,

            "thumb": thumb,

            "index": index

        }

    # -------------------------------------------------
    # Reset
    # -------------------------------------------------

    def reset(self):

        self.pinch_counter = 0
        self.is_grabbing = False