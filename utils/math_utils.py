"""
==========================================================
MorphMotion AI
Math Utility Functions
==========================================================
"""

import math


def distance(point1, point2):
    """
    Calculate Euclidean distance between two points.

    Parameters:
        point1 -> (x, y)
        point2 -> (x, y)

    Returns:
        float
    """
    return math.hypot(point2[0] - point1[0],
                      point2[1] - point1[1])


def midpoint(point1, point2):
    """
    Returns midpoint between two points.
    """

    x = (point1[0] + point2[0]) // 2
    y = (point1[1] + point2[1]) // 2

    return (x, y)


def clamp(value, minimum, maximum):
    """
    Restrict value between minimum and maximum.
    """

    return max(minimum, min(value, maximum))


def interpolate(start, end, alpha):
    """
    Linear interpolation.

    alpha = 0 → start
    alpha = 1 → end
    """

    return start + (end - start) * alpha


def normalize_vector(x, y):
    """
    Returns normalized vector.
    """

    length = math.sqrt(x * x + y * y)

    if length == 0:
        return (0, 0)

    return (x / length, y / length)


def angle(point1, point2):
    """
    Returns angle (degrees)
    between two points.
    """

    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]

    return math.degrees(math.atan2(dy, dx))
