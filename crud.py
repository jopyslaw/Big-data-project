from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from models import WeatherData

class Crud:
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri)
        #self.recreate_database()

    
    def insert_rows_to_db(self, data):
        Session = sessionmaker(bind=self.engine)

        s = Session()
        hourly = data['hourly']

        time = hourly['time']
        temp = hourly['temperature_2m']

        for tm,tem in zip(time,temp):
            d = WeatherData(
                latitude = data['latitude'],
                longtitude = data['longitude'],
                timezone = data['timezone'],
                hour = tm,
                temperature = tem 
            )
            s.add(d)

        s.commit()
        s.close()
        print('Added data')
    
    def recreate_database(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)


