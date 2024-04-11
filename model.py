import tensorflow_decision_forests as tfdf
import keras
from keras.layers import Dense, Activation
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from merge_data import merged_dep_weather_data, merged_arr_weather_data
from process_flight_data import process_flight_data
import pandas as pd
import numpy as np

dep_weather = merged_dep_weather_data()
arr_weather = merged_arr_weather_data()

dep_weather.to_csv('dep_weather.csv', index=False)
arr_weather.to_csv('arr_weather.csv', index=False)

# dep_columns = ['date', 'time', 'flight_number', 'airline', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions']
# dep_weather = dep_weather[dep_columns]
# arr_columns = ['date', 'time', 'flight_number', 'airline', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
# arr_weather = arr_weather[arr_columns]
# dep_encode_col = ['date', 'time', 'flight_number', 'airline', 'destination' ,'conditions', 'label']
# for feather in dep_encode_col:
#     le = LabelEncoder()
#     dep_weather[feather] = le.fit_transform(dep_weather[feather])

# X = dep_weather[dep_columns]
# y = dep_weather['label']
# X_train, X_test, y_train, y_test = train_test_split(X, y)

# X_train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(X_train, label='label')

# pass_dep_model = keras.Sequential()
# pass_dep_model.add(Dense(2048, activation='relu'))
# pass_dep_model.add(Dense(1024, activation='relu'))
# pass_dep_model.add(Dense(512, activation='relu'))
# pass_dep_model.add(Dense(256, activation='relu'))
# pass_dep_model.add(Dense(128, activation='relu'))
# pass_dep_model.add(Dense(64, activation='relu'))
# pass_dep_model.add(Dense(32, activation='relu'))
# pass_dep_model.add(Dense(16, activation='relu'))
# pass_dep_model.add(Dense(8, activation='relu'))
# pass_dep_model.add(Dense(6, activation='softmax'))

# pass_dep_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# pass_dep_model.fit(X_train, y_train, epochs=2000, batch_size=125, verbose=2)
# print(pass_dep_model.evaluate(X_test, y_test)[1])