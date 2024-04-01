import numpy as np
import pandas as pd
import tensorflow_decision_forests as tfdf
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from merge_data import merged_dep_weather_data, merged_arr_weather_data
from process_flight_data import process_flight_data

dep_weather = merged_dep_weather_data()
arr_weather = merged_arr_weather_data()

dep_columns = ['time', 'flight_number', 'airline', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
dep_weather = dep_weather[dep_columns]
arr_columns = ['time', 'flight_number', 'airline', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
arr_weather = arr_weather[arr_columns]

# Binarize the label column
le = LabelEncoder()
dep_weather['label'] = le.fit_transform(dep_weather['label'])
le = LabelEncoder()
arr_weather['label'] = le.fit_transform(arr_weather['label'])

label_col_name = 'label'

train_df, test_df = train_test_split(dep_weather)

train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_df, label=label_col_name)
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_df, label=label_col_name)

NUM_EPOCHS = 20
BATCH_SIZE = 64

model = tfdf.keras.RandomForestModel(
    verbose=2,
    num_trees = 300,
    # split_axis="SPARSE_OBLIQUE",
    # sparse_oblique_normalization="MIN_MAX",
    categorical_algorithm="RANDOM",
    winner_take_all=False
)
model.fit(train_ds, num_epochs=NUM_EPOCHS, batch_size=BATCH_SIZE)
model.compile(metrics=["accuracy"])
evaluation = model.evaluate(test_ds, return_dict=True, batch_size=BATCH_SIZE)
for name, value in evaluation.items():
    print(f"{name}: {value:.4f}")
    
# model.summary()
important_var = model.make_inspector().variable_importances()
print(important_var['INV_MEAN_MIN_DEPTH'])
model.save("model/dep_weather_model", save_format="h5")

# for variable in important_var:
#     print(variable['INV_MEAN_MIN_DEPTH'])
#     print(variable['NUM_AS_ROOT'])
#     print(variable['SUM_SCORE'])
#     print(variable['NUM_NODES'])


train_df, test_df = train_test_split(arr_weather)

train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_df, label=label_col_name)
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_df, label=label_col_name)

NUM_EPOCHS = 20
BATCH_SIZE = 64

model = tfdf.keras.RandomForestModel(
    verbose=2,
    num_trees = 300,
    # split_axis="SPARSE_OBLIQUE",
    # sparse_oblique_normalization="MIN_MAX",
    categorical_algorithm="RANDOM",
    winner_take_all=False
)
model.fit(train_ds, num_epochs=NUM_EPOCHS, batch_size=BATCH_SIZE)
model.compile(metrics=["accuracy"])
evaluation = model.evaluate(test_ds, return_dict=True, batch_size=BATCH_SIZE)
for name, value in evaluation.items():
    print(f"{name}: {value:.4f}")

important_var = model.make_inspector().variable_importances()
print(important_var['INV_MEAN_MIN_DEPTH'])
model.save("model/arr_weather_model", save_format="h5")