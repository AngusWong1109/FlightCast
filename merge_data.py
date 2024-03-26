import pandas as pd
from process_flight_data import process_pass_arr_data, process_pass_dep_data

# Access processed passenger arrival data
pass_arr = process_pass_arr_data('pass_arrival_data.csv')

# Access processed passenger departure data
pass_dep = process_pass_dep_data('pass_departure_data.csv')

# Access processed weather data
weather_data = pd.read_csv('processed_weather_data.csv')
# Change the date in the datat to datetime object
weather_data.loc[:, 'datetime'] = pd.to_datetime(weather_data['datetime'])