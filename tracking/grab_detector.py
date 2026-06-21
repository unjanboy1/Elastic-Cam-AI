"""
==========================================================
MorphMotion AI
Grab Detection Module
----------------------------------------------------------
Finds the closest body or face landmark to the
user's pinch position.
==========================================================
"""

import math


class GrabDetector:

    def __init__(self, max_grab_distance=50):
        """
        max_grab_distance:
            Maximum distance (pixels) allowed between
            pinch center and a landmark to consider it grabbed.
        """
        self.max_grab_distance = max_grab_distance

    # -------------------------------------------------
    # Euclidean Distance
    # -------------------------------------------------

    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    # -------------------------------------------------
    # Find Closest Landmark
    # -------------------------------------------------

    def find_closest_landmark(self, pinch_center, landmarks):

        """
        Parameters
        ----------
        pinch_center : tuple (x, y)

        landmarks :
        [
            [id, x, y],
            ...
        ]

        Returns
        -------
        dict
        """

        if pinch_center is None:
            return None

        if len(landmarks) == 0:
            return None

        px, py = pinch_center

        closest = None
        minimum_distance = float("inf")

        for landmark in landmarks:

            idx = landmark[0]
            x = landmark[1]
            y = landmark[2]

            d = self.distance(px, py, x, y)

            if d < minimum_distance:
                minimum_distance = d
                closest = landmark

        if minimum_distance > self.max_grab_distance:
            return None

        return {
            "id": closest[0],
            "x": closest[1],
            "y": closest[2],
            "distance": minimum_distance
        }

    # -------------------------------------------------
    # Face Grab
    # -------------------------------------------------

    def detect_face_grab(self, pinch_center, face_landmarks):

        landmark = self.find_closest_landmark(
            pinch_center,
            face_landmarks
        )

        if landmark is None:
            return None

        landmark["type"] = "face"

        return landmark

    # -------------------------------------------------
    # Body Grab
    # -------------------------------------------------

    def detect_body_grab(self, pinch_center, pose_landmarks):

        landmark = self.find_closest_landmark(
            pinch_center,
            pose_landmarks
        )

        if landmark is None:
            return None

        landmark["type"] = "body"

        return landmark