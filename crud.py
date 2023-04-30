from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from models import WeatherData

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
        results = session.query(WeatherData.hour, WeatherData.temperature, WeatherData.apparent_temperature).all()
        hours = [result.hour for result in results]
        temperatures = [result.temperature for result in results]
        apparent_temperatures = [result.apparent_temperature for result in results]
        return hours, temperatures, apparent_temperatures


    def get_rain(self):
        session = self.Session()
        results = session.query(WeatherData.hour, WeatherData.precipitation, WeatherData.rain).all()

        # przypisanie kolumn do zmiennych
        hours = [result.hour for result in results]
        precipitations = [result.precipitation for result in results]
        rains = [result.rain for result in results]
        return hours, precipitations, rains
    

    def get_precipitation(self):
        session = self.Session()
        results = session.query(WeatherData.precipitation).all()
        precipitations = [result.precipitation for result in results]
        return precipitations


