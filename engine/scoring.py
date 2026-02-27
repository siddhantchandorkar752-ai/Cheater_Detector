import time

class SuspicionScore:
    def __init__(self, threshold_seconds=3.0):
        # 3 second continuous rule
        self.threshold = threshold_seconds
        self.start_time = None
        self.is_cheating = False

    def update(self, behavior_status):
        if behavior_status in ["Looking Left!", "Looking Right!"]:
            if self.start_time is None:
                self.start_time = time.time() 
            elif (time.time() - self.start_time) > self.threshold:
                self.is_cheating = True 
        else:
            self.start_time = None
            self.is_cheating = False

        return self.is_cheating