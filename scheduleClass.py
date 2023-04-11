from request import ApiConnector
from crud import Crud
from os import environ
from dotenv import load_dotenv
from scheduler import Scheduler
import datetime as dt

load_dotenv()

class Schedule:
    def __init__(self):
        self.crud = Crud(environ.get('DATABASE_URI'))
        self.api = ApiConnector(environ.get('WEATHER_API_URL'))
        self.schedule = Scheduler()
        self.is_running = True
        self.schedule.daily(dt.time(20,44), self.run)
        self.start()
        
    
    def start(self):
        while self.is_running:
            self.schedule.exec_jobs()

    def run(self):
        print('im working')
        data = self.api.get_weather_data()
        self.crud.insert_rows_to_db(data)

    def __del__(self):
        print('Program is not running')
        self.is_running = False
