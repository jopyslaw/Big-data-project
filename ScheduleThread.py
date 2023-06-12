import threading

class ScheduleThread(threading.Thread):
    def __init__(self, schedule):
        super().__init__()
        self.should_run = True
        self.schedule = schedule
    
    def run(self):
        while self.should_run:
            self.schedule.start()

    def stop(self):
        self.schedule.stop()
        self.should_run = False