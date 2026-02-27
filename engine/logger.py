import csv
import os
from datetime import datetime

class AuditLogger:
    def __init__(self, log_file="cheating_logs.csv"): # Seedha bahar save hoga, no folder issue!
        self.log_file = log_file
        
        # Agar file nayi hai toh headers daal do
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Event", "Status"])

    def log_event(self, event_type, status):
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), event_type, status])
        print(f"[AUDIT LOG] {event_type} - {status}")