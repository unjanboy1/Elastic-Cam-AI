import cv2

class Effects:
    def blur(self, frame):
        return cv2.GaussianBlur(frame, (15, 15), 0)

    def highlight(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)