import tensorflow as tf
import keras
from keras.layers.core import Dense, Activation
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from merge_data import merged_dep_weather_data, merged_arr_weather_data
from process_flight_data import process_flight_data

import pandas as pd
import numpy as np

dep_weather = merged_dep_weather_data()
arr_weather = merged_arr_weather_data()

dep_columns = ['time', 'flight_number', 'airline', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
dep_weather = dep_weather[dep_columns]
arr_columns = ['time', 'flight_number', 'airline', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
arr_weather = arr_weather[arr_columns]

# pass_dep_model = keras.Sequential()
# pass_dep_model.add(Dense(2048))
# pass_dep_model.add(Dense(6), activation='softmax')