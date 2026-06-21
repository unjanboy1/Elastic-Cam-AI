"""
==========================================================
MorphMotion AI
Mesh Warp
----------------------------------------------------------
Moves mesh vertices according to the grab point.
==========================================================
"""

import numpy as np


class MeshWarp:

    def __init__(self, influence_radius=120):

        self.radius = influence_radius

    def warp(self, mesh_points, grab_point, current_hand):

        """
        Parameters

        mesh_points : list[(x,y)]

        grab_point : (x,y)

        current_hand : (x,y)

        Returns

        warped mesh
        """

        if grab_point is None:

            return mesh_points

        gx, gy = grab_point

        hx, hy = current_hand

        dx = hx - gx
        dy = hy - gy

        warped = []

        for point in mesh_points:

            x, y = point

            distance = np.sqrt((x-gx)**2 + (y-gy)**2)

            if distance < self.radius:

                influence = 1 - (distance / self.radius)

                nx = x + dx * influence

                ny = y + dy * influence

            else:

                nx = x
                ny = y

            warped.append((int(nx), int(ny)))

        return warped

    def reset(self, mesh_points):

        return mesh_points