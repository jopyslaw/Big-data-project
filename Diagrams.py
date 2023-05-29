import matplotlib.pyplot as plt
import numpy as np


class WeatherDiagrams:
    def __init__(self, app_managment):
        self.app_managment = app_managment
        plt.style.use('ggplot')
    

    def temp_to_app_temp_diagram(self):
        hours, temperatures, apparent_temperatures = self.app_managment.crud.get_temp()

        fig,ax = plt.subplots()
        ax.plot(hours, temperatures, label='Temperature')
        ax.plot(hours, apparent_temperatures, label='Apparent Temperature')
        ax.set_title('Comparison of Temperature and Apparent Temperature')
        ax.set_xlabel('Hours')
        ax.set_ylabel('Temperature (°C)')
        ax.legend()

        # wyświetlenie wykresu
        plt.show()
    
    def rain_to_precipitations_diagram(self):
        hours, precipitations, rains = self.app_managment.crud.get_rain()

        fig, ax = plt.subplots()

        # dodanie danych do wykresu
        ax.plot(hours, precipitations, label='Precipitation')
        ax.plot(hours, rains, label='Rain')

        # dodanie tytułu i etykiet osi
        ax.set_title('Comparison of Precipitation and Rain')
        ax.set_xlabel('Hours')
        ax.set_ylabel('Amount (mm)')

        # dodanie legendy
        ax.legend()

        # wyświetlenie wykresu
        plt.show()
    

    def temperature_std_diagram(self):
        hours, temperatures, apparent_temperatures = self.app_managment.crud.get_temp()
        temperature_std = np.std(temperatures)
        apparent_temperature_std = np.std(apparent_temperatures)

        fig, ax = plt.subplots()

        # dodanie danych do wykresu z odchyleniem standardowym
        ax.errorbar(hours, temperatures, yerr=temperature_std, label='Temperature')
        ax.errorbar(hours, apparent_temperatures, yerr=apparent_temperature_std, label='Apparent Temperature')

        # dodanie tytułu i etykiet osi
        ax.set_title('Standard Deviation of Temperature and Apparent Temperature')
        ax.set_xlabel('Hours')
        ax.set_ylabel('Temperature (°C)')

        # dodanie legendy
        ax.legend()

        # wyświetlenie wykresu
        plt.show()
    
    def temp_histogram(self):
        precipitations = self.app_managment.crud.get_precipitation()

        fig, ax = plt.subplots()
        ax.hist(precipitations, bins=10)

        # dodanie tytułu i etykiet osi
        ax.set_title('Histogram of Precipitation')
        ax.set_xlabel('Precipitation (mm)')
        ax.set_ylabel('Frequency')

        # wyświetlenie histogramu
        plt.show()
    
    def temp(self):
        dates, avg_temperatures = self.app_managment.crud.temp2()

        plt.plot(dates, avg_temperatures)
        plt.xlabel('Days')
        plt.ylabel('Average Temperature')
        plt.title('Average Temperature by Days')
        plt.show()
