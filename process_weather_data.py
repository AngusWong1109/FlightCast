import pandas as pd
import datetime as dt

weather_data = pd.read_csv('weather_data.csv')
new_weather_data = weather_data[weather_data['name'] != 'name']
selected_columns = ['datetime', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'preciptype', 'snow', 'snowdepth', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'icon']
weather_data = new_weather_data[selected_columns]
weather_data.loc[:, 'datetime'] = pd.to_datetime(weather_data['datetime'])
df_file = weather_data.to_csv('processed_weather_data.csv')