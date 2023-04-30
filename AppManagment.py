from request import ApiConnector
from crud import Crud
from os import environ
from dotenv import load_dotenv


class AppManagment():
    def __init__(self):
        self.crud = Crud(environ.get('DATABASE_URI'))
        self.api = ApiConnector(environ.get('WEATHER_API_URL'))
    

    def run(self):
        print('im working')
        data = self.api.get_weather_data()
        self.crud.insert_rows_to_db(data)
    

    def __del__(self):
        print('Program is not running')
        self.is_running = False