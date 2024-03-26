import pandas as pd
import datetime as dt

def process_weather_data(filepath):
    weather_data = pd.read_csv(filepath)
    weather_data = weather_data[weather_data['name'] != 'name']
    selected_columns = ['datetime', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'preciptype', 'snow', 'snowdepth', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'icon']
    weather_data = weather_data[selected_columns]
    return weather_data