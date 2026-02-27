import cv2
import math
import os
from ultralytics import YOLO

class BehaviorAnalyzer:
    def __init__(self):
        openvino_path = 'yolov8n-pose_openvino_model'
        # Bulletproof load
        if os.path.exists(openvino_path):
            self.model = YOLO(openvino_path)
        else:
            self.model = YOLO('yolov8n-pose.pt')

    # Do points ke beech ka distance nikalne ka formula
    def calculate_distance(self, p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def process_frame(self, frame):
        results = self.model(frame, conf=0.5, verbose=False)
        annotated_frame = results[0].plot()

        # Default Status
        suspicious_behavior = "Normal"
        color = (0, 255, 0) # Green

        # Bulletproof Check: Agar koi insaan screen par hai tabhi math lagao
        if results[0].keypoints is not None and len(results[0].keypoints.xy) > 0:
            keypoints = results[0].keypoints.xy[0] # Pehle insaan ka data

            # Ensure karo ki kam se kam 5 points (Nose aur Ears) detect hue hain
            if len(keypoints) >= 5:
                nose = keypoints[0]
                l_ear = keypoints[3]
                r_ear = keypoints[4]

                # Ensure karo ki YOLO ne in points ko actual me detect kiya hai
                if nose[0] != 0 and l_ear[0] != 0 and r_ear[0] != 0:
                    dist_nose_left_ear = self.calculate_distance(nose, l_ear)
                    dist_nose_right_ear = self.calculate_distance(nose, r_ear)

                    # LOGIC: Looking Left / Right ONLY
                    if dist_nose_right_ear > 0 and dist_nose_left_ear > 0:
                        ratio = dist_nose_left_ear / dist_nose_right_ear
                        
                        # Agar naak right kaan ke bohot paas hai
                        if ratio > 2.5:
                            suspicious_behavior = "Looking Right!"
                            color = (0, 0, 255) # Red
                        # Agar naak left kaan ke bohot paas hai
                        elif ratio < 0.4:
                            suspicious_behavior = "Looking Left!"
                            color = (0, 0, 255) # Red

        return annotated_frame, suspicious_behavior, color