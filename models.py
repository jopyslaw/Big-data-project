from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Double, TIMESTAMP, DATETIME, Float
from sqlalchemy.sql.functions import current_timestamp
from dotenv import load_dotenv
from os import environ

Base = declarative_base()

load_dotenv()

class WeatherData(Base):
    __tablename__ = environ.get('DB_NAME')
    
    id = Column(Integer, primary_key=True, autoincrement="auto")
    latitude = Column(Double)
    longtitude = Column(Double)
    timezone = Column(String)
    hour = Column(TIMESTAMP)
    temperature = Column(Float)
    apparent_temperature = Column(Float)
    precipitation = Column(Float)
    rain = Column(Float)
    weathercode = Column(Integer)
    cloudcover = Column(Integer)
    visibility = Column(Integer)
    windspeed_180m = Column(Float)
    winddirection_180m = Column(Float)
    windgusts_10m = Column(Float)
    temperature_2m_unit = Column(String)
    apparent_temperature_unit = Column(String)
    precipitation_unit = Column(String)
    rain_unit = Column(String)
    weathercode_unit = Column(String)
    cloudcover_unit = Column(String)
    visibility_unit = Column(String)
    windspeed_180m_unit = Column(String)
    winddirection_180m_unit = Column(String)
    windgusts_10m_unit = Column(String)
    creation_time = Column(TIMESTAMP, default=current_timestamp())


    __table_args__ = {'schema': 'big_data'}