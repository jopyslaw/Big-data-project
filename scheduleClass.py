from request import ApiConnector
from crud import Crud
from os import environ
from dotenv import load_dotenv
from scheduler import Scheduler
import datetime as dt

load_dotenv()

class Schedule:
    def __init__(self, appManagment):
        self.appManagment = appManagment
        self.schedule = Scheduler()
        self.is_running = False
        self.schedule.daily(dt.time(3,0), self.run)
    
    def start(self):
        self.is_running = True
        while self.is_running:
            self.schedule.exec_jobs()

    def run(self):
        print('im working')
        self.appManagment.run()

    def __del__(self):
        print('Program is not running')
        self.is_running = False
    
    def stop(self):
        self.is_running = False
