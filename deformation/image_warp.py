import cv2
import numpy as np

class ImageWarp:
    def warp(self, frame, src_points, dst_points):
        """
        Warp image using perspective transform (basic version)
        """

        if len(src_points) < 4 or len(dst_points) < 4:
            return frame

        src = np.float32(src_points[:4])
        dst = np.float32(dst_points[:4])

        matrix = cv2.getPerspectiveTransform(src, dst)
        warped = cv2.warpPerspective(frame, matrix, (frame.shape[1], frame.shape[0]))

        return warped