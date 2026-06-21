import cv2

class Controls:
    def __init__(self):
        self.running = True

    def handle_keys(self):
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            self.running = False

        return self.running