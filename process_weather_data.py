import pandas as pd
import datetime as dt

def process_weather_data(filepath):
    weather_data = pd.read_csv(filepath)
    weather_data = weather_data[weather_data['name'] != 'name']
    selected_columns = ['datetime', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions']
    weather_data = weather_data[selected_columns]
    # Change the date in the datat to datetime object
    weather_data.loc[:, 'datetime'] = pd.to_datetime(weather_data['datetime'])
    return weather_data