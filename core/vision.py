import cv2
import threading
import time

class CameraStream:
    def __init__(self, src=0):
        # src=0 matlab laptop ka default webcam. 
        # Baad mein hum isko IP/CCTV camera ki RTSP link se replace kar sakte hain.
        self.stream = cv2.VideoCapture(src)
        
        # Resolution set karna (640x480 is best for i3 CPU processing)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        # Background thread start karna jo camera ko handle karegi
        threading.Thread(target=self.update, args=(), daemon=True).start()
        return self

    def update(self):
        # Jab tak system chalu hai, background mein frames grab karte raho
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # AI engine ko latest frame dena
        return self.frame

    def stop(self):
        # System band karna
        self.stopped = True
        self.stream.release()