from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Double, TIMESTAMP, DATE, Float
from dotenv import load_dotenv
from os import environ


Base = declarative_base()

load_dotenv()

class WeatherData(Base):
    __tablename__ = environ.get('DB_NAME')
    id = Column(Integer, primary_key=True)
    latitude = Column(Double)
    longtitude = Column(Double)
    timezone = Column(String)
    hour = Column(DATE)
    temperature = Column(Float)
    #creation_time = Column(TIMESTAMP, default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    __table_args__ = {'schema': 'big_data'}