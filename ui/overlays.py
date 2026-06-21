import cv2

class Overlays:
    def draw_text(self, frame, text, pos=(50, 50)):
        cv2.putText(
            frame,
            text,
            pos,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        return frame

    def draw_box(self, frame, x, y, w, h):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return frame