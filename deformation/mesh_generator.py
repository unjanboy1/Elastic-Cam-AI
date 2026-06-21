"""
==========================================================
MorphMotion AI
Mesh Generator
----------------------------------------------------------
Creates Delaunay Triangle Mesh
==========================================================
"""

import cv2
import numpy as np


class MeshGenerator:

    def __init__(self):
        pass

    def create_mesh(self, frame, mesh_points):

        h, w = frame.shape[:2]

        rect = (0, 0, w, h)

        subdiv = cv2.Subdiv2D(rect)

        # Insert points
        for point in mesh_points:

            try:
                subdiv.insert(point)
            except:
                pass

        triangles = subdiv.getTriangleList()

        triangle_indices = []

        for triangle in triangles:

            pts = [

                (triangle[0], triangle[1]),

                (triangle[2], triangle[3]),

                (triangle[4], triangle[5])

            ]

            indices = []

            for p in pts:

                for i, mesh in enumerate(mesh_points):

                    if abs(mesh[0] - p[0]) < 1 and abs(mesh[1] - p[1]) < 1:

                        indices.append(i)

                        break

            if len(indices) == 3:

                triangle_indices.append(indices)

        return triangle_indices

    def draw_mesh(self, frame, mesh_points, triangles):

        for tri in triangles:

            p1 = mesh_points[tri[0]]
            p2 = mesh_points[tri[1]]
            p3 = mesh_points[tri[2]]

            cv2.line(frame, p1, p2, (255, 0, 0), 1)
            cv2.line(frame, p2, p3, (255, 0, 0), 1)
            cv2.line(frame, p3, p1, (255, 0, 0), 1)

        return frame