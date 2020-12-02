"""
File that contains code to check the weather of a city, and return an object with the details
"""

import requests


class CityWeather:
    """
    Object that contains the information about the city
    """

    def __init__(self, city_name, long=None, lat=None, temperature=None, feels_like=None,
                 humidity=None, pressure=None, report=None,
                 wind_speed=None, wind_direction=None):
        self.lat = lat
        self.long = long
        self.city_name = city_name
        self.temperature = temperature
        self.feels_like = feels_like
        self.humidity = humidity
        self.pressure = pressure
        self.report = report
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def set_temp(self, temperature):
        """
        :param temperature: Temperature of the City
        """
        self.temperature = temperature

    def set_feels_like(self, feels_like):
        """
        :param feels_like: Feels Like temperature of the city
        """
        self.feels_like = feels_like

    def set_humidity(self, humidity):
        """
        :param humidity: Humidity of the  city
        """
        self.humidity = humidity

    def set_pressure(self, pressure):
        """
        :param pressure: Atmospheric Pressure of the city
        """
        self.pressure = pressure

    def set_report(self, report):
        """
        :param report: Weather Report for the city
        """
        self.report = report

    def set_wind_speed(self, wind_speed):
        """
        :param wind_speed: Wind Speed of the city
        """
        self.wind_speed = wind_speed

    def set_wind_direction(self, wind_direction):
        """
        :param wind_direction: Direction the wind is traveling
        """
        self.wind_direction = wind_direction

    def set_long_lat(self, long, lat):
        """
        :param long: Longitude coordinates of city
        :param lat: Latitude coordinates for city
        """
        self.long = long
        self.lat = lat


def get_weather_for_city(city_name):
    """
    Uses the Open Weather Map project to retrieve the weather for a given city
    :param city_name: The city to get a weather report for
    :returns: an object that contains all of the weather data for the city.
    """

    api_key = '1aee813f7d4ebbf8c7b5b9d5d8cfa0a3'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    if ',' in city_name:
        location = city_name.find(',')
        state_code = city_name[(location + 1):].upper().strip()
        city_name = city_name[0:location]
        city = CityWeather(city_name)
        url = f'{base_url}q={city_name},{state_code},US&appid={api_key}&units=imperial'
    else:
        city = CityWeather(city_name)
        url = f'{base_url}q={city_name}&appid={api_key}&units=imperial'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        coord = data['coord']

        city.set_temp(main['temp'])
        city.set_feels_like(main['feels_like'])
        city.set_humidity(main['humidity'])
        city.set_pressure(main['pressure'])
        city.set_report(data['weather'][0]['description'])
        city.set_wind_speed(wind['speed'])
        city.set_wind_direction(wind['deg'])
        city.set_long_lat(coord['lon'], coord['lat'])
    else:
        raise ConnectionRefusedError

    return city
