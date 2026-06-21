"""
==========================================================
MorphMotion AI
Body Mesh Module
----------------------------------------------------------
Creates a deformable mesh from MediaPipe landmarks.

Author : Zaib
==========================================================
"""

import cv2
import numpy as np


class BodyMesh:

    def __init__(self):

        self.mesh_points = []

    # ----------------------------------------------------
    # Clear Mesh
    # ----------------------------------------------------

    def clear(self):

        self.mesh_points = []

    # ----------------------------------------------------
    # Build Mesh
    # ----------------------------------------------------

    def build(self, pose_landmarks, face_landmarks):

        """
        Creates one unified mesh consisting of

        - Pose landmarks
        - Face landmarks

        Returns
        -------
        list[(x,y)]
        """

        self.mesh_points = []

        # ------------------------
        # Body
        # ------------------------

        for point in pose_landmarks:

            self.mesh_points.append(
                (point[1], point[2])
            )

        # ------------------------
        # Face
        # ------------------------

        for point in face_landmarks:

            self.mesh_points.append(
                (point[1], point[2])
            )

        return self.mesh_points

    # ----------------------------------------------------
    # Get Mesh
    # ----------------------------------------------------

    def get_mesh(self):

        return self.mesh_points

    # ----------------------------------------------------
    # Draw Mesh
    # ----------------------------------------------------

    def draw(self, frame):

        for point in self.mesh_points:

            cv2.circle(
                frame,
                point,
                2,
                (0,255,255),
                -1
            )

        return frame

    # ----------------------------------------------------
    # Number of Mesh Vertices
    # ----------------------------------------------------

    def size(self):

        return len(self.mesh_points)