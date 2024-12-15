import cv2
import threading

class VideoCaptureThread:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)
        if not self.cap.isOpened():
            raise ValueError("Unable to open video source")
        self.frame = None
        self.running = True
        self.lock = threading.Lock()

        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while self.running:
            success, frame = self.cap.read()
            if success:
                with self.lock:
                    self.frame = frame
            else:
                print("Failed to capture frame")

    def read(self):
        with self.lock:
            return self.frame

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()
