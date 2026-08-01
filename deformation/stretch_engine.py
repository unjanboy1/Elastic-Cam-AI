import numpy as np

class StretchEngine:
    def __init__(self, strength=0.5):
        self.strength = strength


    def apply_stretch(self, image, points, anchor_point):
        """
        Simple fake stretch effect using point displacement.
        image: frame
        points: landmarks or pixels
        anchor_point: fixed reference point
        """

        stretched_points = []

        ax, ay = anchor_point

        for (x, y) in points:
            dx = x - ax
            dy = y - ay

            # stretch formula (scaled displacement)
            new_x = int(ax + dx * self.strength)
            new_y = int(ay + dy * self.strength)

            stretched_points.append((new_x, new_y))

        return stretched_points