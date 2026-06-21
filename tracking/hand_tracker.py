import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

        all_hands = []

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = frame.shape
                    lm_list.append((id, int(lm.x * w), int(lm.y * h)))

                all_hands.append(lm_list)

                self.mp_draw.draw_landmarks(
                    frame, handLms, self.mp_hands.HAND_CONNECTIONS
                )

        return all_hands