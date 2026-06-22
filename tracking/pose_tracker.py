"""
==========================================================
MorphMotion AI
Pose Tracking Module
----------------------------------------------------------
Uses MediaPipe Pose to detect and track body landmarks.
==========================================================
"""


import cv2
import mediapipe as mp

from config import (
    POSE_DETECTION_CONFIDENCE,
    POSE_TRACKING_CONFIDENCE,
    SHOW_POSE_LANDMARKS
)


class PoseTracker:

    def __init__(self):

        self.mpPose = mp.solutions.pose

        self.pose = self.mpPose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            min_detection_confidence=POSE_DETECTION_CONFIDENCE,
            min_tracking_confidence=POSE_TRACKING_CONFIDENCE
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.results = None

    # -------------------------------------------------
    # Detect Pose
    # -------------------------------------------------

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.pose.process(rgb)

        if SHOW_POSE_LANDMARKS:
            self.draw(frame)

        return frame

    # -------------------------------------------------
    # Draw Landmarks
    # -------------------------------------------------

    def draw(self, frame):

        if self.results and self.results.pose_landmarks:

            self.mpDraw.draw_landmarks(
                frame,
                self.results.pose_landmarks,
                self.mpPose.POSE_CONNECTIONS
            )

    # -------------------------------------------------
    # Return All Body Landmarks
    # -------------------------------------------------

    def get_landmarks(self, frame):

        landmark_list = []

        if self.results is None:
            return landmark_list

        if self.results.pose_landmarks:

            h, w, _ = frame.shape

            for idx, lm in enumerate(self.results.pose_landmarks.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                landmark_list.append([
                    idx,
                    cx,
                    cy,
                    lm.visibility
                ])

        return landmark_list

    # -------------------------------------------------
    # Get Specific Landmark
    # -------------------------------------------------

    def get_landmark(self, frame, landmark_id):

        landmarks = self.get_landmarks(frame)

        for point in landmarks:

            if point[0] == landmark_id:
                return point

        return None

    # -------------------------------------------------
    # Check if Body Detected
    # -------------------------------------------------

    def body_detected(self):

        return (
            self.results is not None
            and self.results.pose_landmarks is not None
        )

    # -------------------------------------------------
    # Close MediaPipe
    # -------------------------------------------------

    def close(self):

        self.pose.close()