from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from models import WeatherData
import pandas as pd
from sqlalchemy.sql import func
from datetime import datetime

class Crud:
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri)
        self.Session = sessionmaker(bind=self.engine)
        #self.recreate_database()

    
    def insert_rows_to_db(self, data):
        print(data)
        s = self.Session()
        hourly = data['hourly']
        hourly_units = data['hourly_units']

        time = hourly['time']
        temp = hourly['temperature_2m']
        apparent_temp = hourly['apparent_temperature']
        precipitation = hourly['precipitation']
        rain = hourly['rain']
        weathercode = hourly['weathercode']
        cloudcover = hourly['cloudcover']
        visibility = hourly['visibility']
        windspeed_180m = hourly['windspeed_180m']
        winddirection_180m = hourly['winddirection_180m']
        windgusts_10m = hourly['windgusts_10m']

        for tm,tem,app_temp,preci,rai,weatherCode,cloudCover,visib,windSpd180,windDirect180,windgust10 in zip(time,temp,apparent_temp,precipitation,rain,weathercode,cloudcover,visibility,windspeed_180m,winddirection_180m, windgusts_10m):
            d = WeatherData(
                latitude = data['latitude'],
                longtitude = data['longitude'],
                timezone = data['timezone'],
                hour = tm,
                temperature = tem,
                apparent_temperature = app_temp,
                precipitation = preci,
                rain = rai,
                weathercode = weatherCode,
                cloudcover = cloudCover,
                visibility = visib,
                windspeed_180m = windSpd180,
                winddirection_180m = windDirect180,
                windgusts_10m = windgust10,
                temperature_2m_unit = hourly_units['temperature_2m'],
                apparent_temperature_unit = hourly_units['apparent_temperature'],
                precipitation_unit = hourly_units['precipitation'],
                rain_unit = hourly_units['rain'],
                weathercode_unit = hourly_units['weathercode'],
                cloudcover_unit = hourly_units['cloudcover'],
                visibility_unit = hourly_units['visibility'],
                windspeed_180m_unit = hourly_units['windspeed_180m'],
                winddirection_180m_unit = hourly_units['winddirection_180m'],
                windgusts_10m_unit = hourly_units['windgusts_10m']
            )
            s.add(d)

        s.commit()
        s.close()
        print('Added data')
    
    def recreate_database(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
    

    def get_temp(self):
        session = self.Session()
        # Pobranie danych grupujących po dacie (bez godziny i minut) i obliczenie średniej temperatury dla każdej grupy
        query = session.query(func.avg(WeatherData.temperature), func.date(WeatherData.creation_time), func.avg(WeatherData.apparent_temperature)).group_by(func.date(WeatherData.creation_time)).order_by(func.date(WeatherData.creation_time))

        # Wykonanie zapytania i pobranie wyników
        results = query.all()
        
        dates = [result[1] for result in results]
        temperatures = [result[0] for result in results]
        apparent_temperatures = [result[2] for result in results]
        return dates, temperatures, apparent_temperatures


    def get_rain(self):
        session = self.Session()
        query = session.query(func.avg(WeatherData.precipitation), func.date(WeatherData.creation_time), func.avg(WeatherData.rain)).group_by(func.date(WeatherData.creation_time)).order_by(func.date(WeatherData.creation_time))
        #results = session.query(WeatherData.hour, WeatherData.precipitation, WeatherData.rain).all()

        results = query.all()

        dates = [result[1] for result in results]
        avg_rain = [result[2] for result in results]
        avg_precipitation = [result[0] for result in results]

        # przypisanie kolumn do zmiennych
        #hours = [result.hour for result in results]
        #precipitations = [result.precipitation for result in results]
        #rains = [result.rain for result in results]
        return dates, avg_precipitation, avg_rain
    

    def get_precipitation(self):
        session = self.Session()
        results = session.query(WeatherData.precipitation).all()
        precipitations = [result.precipitation for result in results]
        return precipitations
    

    def temp2(self):
        session = self.Session()
        # Pobranie danych grupujących po dacie (bez godziny i minut) i obliczenie średniej temperatury dla każdej grupy
        query = session.query(func.avg(WeatherData.temperature), func.date(WeatherData.creation_time)).group_by(func.date(WeatherData.creation_time)).order_by(func.date(WeatherData.creation_time))

        # Wykonanie zapytania i pobranie wyników
        results = query.all()

        # Podział wyników na dwie listy: daty i średnie temperatury
        dates = [result[1] for result in results]
        avg_temperatures = [result[0] for result in results]

        # Konwersja daty na obiekt datetime
        dates = [datetime.strptime(date.strftime('%Y-%m-%d'), '%Y-%m-%d') for date in dates]

        return dates, avg_temperatures


    def xd(self):
        session = self.Session()
        data = session.query(WeatherData).all()

        print(data)

        # Konwersja danych do ramki danych (DataFrame) w celu łatwiejszej manipulacji
        df = pd.DataFrame([(d.timezone, d.hour.date(), d.temperature, d.apparent_temperature, d.precipitation, d.rain, d.weathercode, d.cloudcover, d.visibility, d.windspeed_180m, d.winddirection_180m, d.windgusts_10m) for d in data],
                        columns=['timezone', 'date', 'temperature', 'apparent_temperature', 'precipitation', 'rain', 'weathercode', 'cloudcover', 'visibility', 'windspeed_180m', 'winddirection_180m', 'windgusts_10m'])

        # Normalizacja danych dla każdego dnia
        #df['normalized_temperature'] = df.groupby('date')['temperature'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_apparent_temperature'] = df.groupby('date')['apparent_temperature'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_precipitation'] = df.groupby('date')['precipitation'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_rain'] = df.groupby('date')['rain'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_weathercode'] = df.groupby('date')['weathercode'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_cloudcover'] = df.groupby('date')['cloudcover'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_visibility'] = df.groupby('date')['visibility'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_windspeed_180m'] = df.groupby('date')['windspeed_180m'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_winddirection_180m'] = df.groupby('date')['winddirection_180m'].transform(lambda x: (x - x.mean()) / x.std())
        #df['normalized_windgusts_10m'] = df.groupby('date')['windgusts_10m'].transform(lambda x: (x - x.mean()) / x.std())

        return df


