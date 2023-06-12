from tkinter import *
from dotenv import load_dotenv
from os import environ
from scheduleClass import Schedule
from threading import *
from AppManagment import AppManagment
from ScheduleThread import ScheduleThread
from Diagrams import WeatherDiagrams

load_dotenv()

class MyGui():
    def __init__(self, master):
        self.master = master
        self.app = Frame(master)
        self.app.grid()
        self.app_managment = AppManagment()
        self.schedule = Schedule(self.app_managment)
        self.create_widgets()
        self.schedule_thread = ScheduleThread(self.schedule)
        self.diagrams = WeatherDiagrams(self.app_managment)
        self.t1 = None
        self.threading()

    def create_widgets(self):
        self.main_label = Label(self.app, text = environ.get('PROGRAM_TITLE'))
        self.main_label.grid(row = 0, column = 1, sticky = N)

        self.update_data = Button(self.app, text=environ.get('UPDATE_DATA'), command=self.update_data)
        self.update_data.grid(row = 1, column = 1, sticky = E)
        self.show_diagram_btn = Button(self.app, text=environ.get('SHOW_DIAGRAM'), command=self.show_diagram)
        self.show_diagram_btn.grid(row = 1, column = 2, sticky = E)

        self.app.pack()
    
    def show_diagram(self):
        self.diagrams.temp_to_app_temp_diagram()
        self.diagrams.rain_to_precipitations_diagram()
        self.diagrams.temperature_std_diagram()
        self.diagrams.temp_histogram()
        self.diagrams.wind()

    def update_data(self):
        self.app_managment.run()

    def threading(self):
        self.schedule_thread.start()
    
    def __del__(self):
        self.schedule_thread.stop()
