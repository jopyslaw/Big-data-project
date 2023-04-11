from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Double, TIMESTAMP, DATE, Float
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
    hour = Column(DATE)
    temperature = Column(Float)
    creation_time = Column(TIMESTAMP, default=current_timestamp())

    __table_args__ = {'schema': 'big_data'}