import cv2
import time
from core.vision import CameraStream
from core.behavior import BehaviorAnalyzer
from engine.scoring import SuspicionScore
from engine.logger import AuditLogger

def main():
    print("[INFO] Booting up Cheater_Detector FINAL Engine...")
    
    # Modules Initialize karna
    analyzer = BehaviorAnalyzer()
    scorer = SuspicionScore(threshold_seconds=3.0) 
    logger = AuditLogger()
    
    print("[INFO] Starting high-speed video stream...")
    cam = CameraStream(src=0).start()
    time.sleep(1.0) 

    prev_time = time.time()
    already_logged = False # Taki CSV mein spam na ho

    try:
        while True:
            frame = cam.read()
            if frame is None:
                continue

            # 1. AI Vision
            annotated_frame, status_text, status_color = analyzer.process_frame(frame)
            
            # 2. AI Brain
            is_cheating = scorer.update(status_text)

            # 3. FPS Calc
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 1
            prev_time = curr_time

            # 4. Standard UI
            cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 40), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 0), 2)
            cv2.putText(annotated_frame, f"Behavior: {status_text}", (20, 75), cv2.FONT_HERSHEY_DUPLEX, 0.7, status_color, 2)

            # 5. Alert & Logging System
            if is_cheating:
                cv2.rectangle(annotated_frame, (0, 0), (annotated_frame.shape[1], annotated_frame.shape[0]), (0, 0, 255), 10)
                cv2.putText(annotated_frame, "ALERT: CHEATING DETECTED!", (40, 200), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 0, 255), 3)
                
                if not already_logged:
                    logger.log_event("Suspicious Activity", status_text)
                    already_logged = True
            else:
                already_logged = False # Reset if normal

            cv2.imshow("Cheater_Detector - Live Surveillance", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user.")
    finally:
        print("[INFO] Cleaning up processes...")
        cam.stop()
        cv2.destroyAllWindows()
        print("[INFO] System offline.")

if __name__ == "__main__":
    main()