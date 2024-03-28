from process_flight_data import process_flight_data
from process_weather_data import process_weather_data
import pandas as pd
import datetime as dt

def label_time(row):
    date_str = row['date'] + ' ' + row['time']
    time = dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    time = time.replace(minute=0)
    return time

def merged_dep_weather_data():
    # Access processed passenger departure data
    pass_dep = process_flight_data('pass_departure_data.csv', arrival=False)
    pass_dep['datetime'] = pass_dep.apply(label_time, axis=1)

    # Access processed weather data
    weather_data = process_weather_data('weather_data.csv')
    weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])

    merged_dep_weather_data = pass_dep.merge(weather_data, how = 'left', on='datetime')
    merged_dep_weather_data = merged_dep_weather_data.drop_duplicates()
    selected_dep_columns = ['date', 'arrival', 'time', 'flight', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'preciptype', 'snow', 'snowdepth', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'icon', 'label']
    dep_weather = merged_dep_weather_data[selected_dep_columns]
    return dep_weather

def merged_arr_weather_data():
    # Access processed passenger arrival data
    pass_arr = process_flight_data('pass_arrival_data.csv')
    pass_arr['datetime'] = pass_arr.apply(label_time, axis=1)

    # Access processed weather data
    weather_data = process_weather_data('weather_data.csv')
    weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])

    merged_arr_weather_data = pass_arr.merge(weather_data, how = 'left', on='datetime')
    merged_arr_weather_data = merged_arr_weather_data.drop_duplicates()
    selected_arr_columns = ['date', 'arrival', 'time', 'flight', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'preciptype', 'snow', 'snowdepth', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'icon', 'label']
    arr_weather = merged_arr_weather_data[selected_arr_columns]
    return arr_weather