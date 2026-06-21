"""
==========================================================
MorphMotion AI
Face Tracking Module
----------------------------------------------------------
Uses MediaPipe Face Mesh to detect and track
468 facial landmarks.
==========================================================
"""

import cv2
import mediapipe as mp

from config import (
    FACE_DETECTION_CONFIDENCE,
    FACE_TRACKING_CONFIDENCE,
    SHOW_FACE_LANDMARKS
)


class FaceTracker:

    def __init__(self):

        self.mpFace = mp.solutions.face_mesh

        self.face_mesh = self.mpFace.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=FACE_DETECTION_CONFIDENCE,
            min_tracking_confidence=FACE_TRACKING_CONFIDENCE
        )

        self.mpDraw = mp.solutions.drawing_utils

        self.results = None

    # -------------------------------------------------
    # Detect Face
    # -------------------------------------------------

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.face_mesh.process(rgb)

        if SHOW_FACE_LANDMARKS:
            self.draw(frame)

        return frame

    # -------------------------------------------------
    # Draw Face Mesh
    # -------------------------------------------------

    def draw(self, frame):

        if self.results is None:
            return

        if self.results.multi_face_landmarks:

            for face in self.results.multi_face_landmarks:

                self.mpDraw.draw_landmarks(
                    image=frame,
                    landmark_list=face,
                    connections=self.mpFace.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mpDraw.DrawingSpec(
                        thickness=1,
                        circle_radius=1
                    )
                )

    # -------------------------------------------------
    # Return All Face Landmarks
    # -------------------------------------------------

    def get_landmarks(self, frame):

        landmark_list = []

        if self.results is None:
            return landmark_list

        if self.results.multi_face_landmarks:

            h, w, _ = frame.shape

            face = self.results.multi_face_landmarks[0]

            for idx, lm in enumerate(face.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                landmark_list.append([
                    idx,
                    cx,
                    cy
                ])

        return landmark_list

    # -------------------------------------------------
    # Get Single Landmark
    # -------------------------------------------------

    def get_landmark(self, frame, landmark_id):

        landmarks = self.get_landmarks(frame)

        for point in landmarks:

            if point[0] == landmark_id:
                return point

        return None

    # -------------------------------------------------
    # Check if Face Exists
    # -------------------------------------------------

    def face_detected(self):

        return (
            self.results is not None
            and self.results.multi_face_landmarks is not None
        )

    # -------------------------------------------------
    # Return Important Face Points
    # -------------------------------------------------

    def get_keypoints(self, frame):

        landmarks = self.get_landmarks(frame)

        if len(landmarks) == 0:
            return {}

        return {

            "nose_tip": landmarks[1][1:],

            "left_eye": landmarks[33][1:],

            "right_eye": landmarks[263][1:],

            "left_cheek": landmarks[234][1:],

            "right_cheek": landmarks[454][1:],

            "chin": landmarks[152][1:],

            "upper_lip": landmarks[13][1:],

            "lower_lip": landmarks[14][1:]
        }

    # -------------------------------------------------
    # Close MediaPipe
    # -------------------------------------------------

    def close(self):

        self.face_mesh.close()