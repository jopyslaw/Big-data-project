import requests

class ApiConnector:
    def __init__(self, url):
        self.url = url
    
    def get_weather_data(self):
        response = requests.get(self.url)
        json_data = response.json()
        return json_data