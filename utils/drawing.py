"""
==========================================================
MorphMotion AI
Drawing Utility Functions
==========================================================
"""

import cv2

from config import (
    GREEN,
    RED,
    BLUE,
    WHITE,
    FONT_SCALE,
    TEXT_THICKNESS,
    LINE_THICKNESS
)


def draw_point(frame, point, color=GREEN, radius=6):

    cv2.circle(
        frame,
        point,
        radius,
        color,
        -1
    )


def draw_line(frame, p1, p2,
              color=BLUE,
              thickness=LINE_THICKNESS):

    cv2.line(
        frame,
        p1,
        p2,
        color,
        thickness
    )


def draw_text(frame,
              text,
              position,
              color=WHITE):

    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        color,
        TEXT_THICKNESS
    )


def draw_rectangle(frame,
                   top_left,
                   bottom_right,
                   color=GREEN,
                   thickness=2):

    cv2.rectangle(
        frame,
        top_left,
        bottom_right,
        color,
        thickness
    )


def draw_grab(frame, point):

    draw_point(frame, point, RED, 10)

    cv2.putText(
        frame,
        "GRAB",
        (point[0] + 15, point[1]),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        RED,
        2
    )


def draw_stretch_line(frame, start, end):

    cv2.arrowedLine(
        frame,
        start,
        end,
        BLUE,
        3
    )