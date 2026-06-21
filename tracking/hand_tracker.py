"""
==========================================================
MorphMotion AI
Hand Tracking Module
----------------------------------------------------------
Uses MediaPipe Hands to detect and track hand landmarks.
==========================================================
"""

import cv2
import mediapipe as mp

from config import (
    HAND_DETECTION_CONFIDENCE,
    HAND_TRACKING_CONFIDENCE,
    SHOW_HAND_LANDMARKS
)


class HandTracker:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=HAND_DETECTION_CONFIDENCE,
            min_tracking_confidence=HAND_TRACKING_CONFIDENCE
        )

        self.mpDraw = mp.solutions.drawing_utils

        self.results = None

    # ---------------------------------------------------
    # Detect Hands
    # ---------------------------------------------------

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb)

        if SHOW_HAND_LANDMARKS:
            self.draw(frame)

        return frame

    # ---------------------------------------------------
    # Draw Landmarks
    # ---------------------------------------------------

    def draw(self, frame):

        if self.results.multi_hand_landmarks:

            for hand_landmarks in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mpHands.HAND_CONNECTIONS
                )

    # ---------------------------------------------------
    # Return Hand Landmark List
    # ---------------------------------------------------

    def get_landmarks(self, frame):

        landmark_list = []

        if self.results is None:
            return landmark_list

        if self.results.multi_hand_landmarks:

            h, w, _ = frame.shape

            for hand_id, hand in enumerate(self.results.multi_hand_landmarks):

                single_hand = []

                for idx, lm in enumerate(hand.landmark):

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    single_hand.append([idx, cx, cy])

                landmark_list.append(single_hand)

        return landmark_list

    # ---------------------------------------------------
    # Return Handedness
    # ---------------------------------------------------

    def get_handedness(self):

        hands = []

        if self.results is None:
            return hands

        if self.results.multi_handedness:

            for hand in self.results.multi_handedness:

                hands.append(
                    hand.classification[0].label
                )

        return hands

    # ---------------------------------------------------
    # Get Fingertips
    # ---------------------------------------------------

    def get_fingertips(self, landmarks):

        tips = {}

        if len(landmarks) != 21:
            return tips

        tips["thumb"] = landmarks[4][1:]
        tips["index"] = landmarks[8][1:]
        tips["middle"] = landmarks[12][1:]
        tips["ring"] = landmarks[16][1:]
        tips["pinky"] = landmarks[20][1:]

        return tips

    # ---------------------------------------------------
    # Check if Hands Detected
    # ---------------------------------------------------

    def hands_detected(self):

        if self.results is None:
            return False

        return self.results.multi_hand_landmarks is not None

    # ---------------------------------------------------
    # Close MediaPipe
    # ---------------------------------------------------

    def close(self):

        self.hands.close()