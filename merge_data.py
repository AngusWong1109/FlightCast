import pandas as pd
from process_flight_data import process_flight_data
from process_weather_data import process_weather_data

# Access processed passenger arrival data
pass_arr = process_flight_data('pass_arrival_data.csv')

# Access processed passenger departure data
pass_dep = process_flight_data('pass_departure_data.csv', arrival=False)

# Access processed weather data
weather_data = process_weather_data('weather_data.csv')