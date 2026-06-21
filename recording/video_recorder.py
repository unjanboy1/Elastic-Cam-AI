import cv2

class VideoRecorder:
    def __init__(self, filename="output.mp4", fps=20, frame_size=(640, 480)):
        self.filename = filename
        self.fps = fps
        self.frame_size = frame_size

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.writer = cv2.VideoWriter(filename, fourcc, fps, frame_size)

    def write(self, frame):
        self.writer.write(frame)

    def stop(self):
        self.writer.release()