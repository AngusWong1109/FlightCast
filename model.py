import numpy as np
import pandas as pd
import tensorflow_decision_forests as tfdf
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from merge_data import merged_dep_weather_data, merged_arr_weather_data
from process_flight_data import process_flight_data

dep_weather = merged_dep_weather_data()
arr_weather = merged_arr_weather_data()

dep_columns = ['time', 'flight_number', 'airline', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
dep_weather = dep_weather[dep_columns]
# Binarize the label column
le = LabelEncoder()
dep_weather['label'] = le.fit_transform(dep_weather['label'])
# le = LabelEncoder()
# arr_weather['label'] = le.fit_transform(arr_weather['label'])

# Encode string data
# date_ohe = OneHotEncoder(sparse_output=False)
time_ohe = OneHotEncoder(sparse_output=False)
flight_number_ohe = OneHotEncoder(sparse_output=False)
airline_ohe = OneHotEncoder(sparse_output=False)
place_ohe = OneHotEncoder(sparse_output=False)
weather_conditions_ohe = OneHotEncoder(sparse_output=False)

transformer = ColumnTransformer(
    [
        # ('date', date_ohe, ['date']),
        ('time', time_ohe, ['time']),
        ('flight_number', flight_number_ohe, ['flight_number']),
        ('airline', airline_ohe, ['airline']),
        ('place', place_ohe, ['destination']),
        ('weather_conditions', weather_conditions_ohe, ['conditions'])
    ],
    remainder='passthrough'
)
dep_weather = transformer.fit_transform(dep_weather)
dep_weather = pd.DataFrame(dep_weather)

column_names = [str(i) for i in range(len(dep_weather.columns))]
dep_weather.columns = column_names
label_col_name = dep_weather.columns[-1]

train_df, test_df = train_test_split(dep_weather)

train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_df, label=label_col_name)
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_df, label=label_col_name)

model = tfdf.keras.RandomForestModel(verbose=2)
model.fit(train_ds)
prediction = model.predict(test_ds)
predictions = pd.Series(np.argmax(prediction, axis=1))
print(predictions.shape)
y_true = test_df[label_col_name]
accuracy = accuracy_score(y_true, predictions)
print(f"Accuracy: {accuracy:.4f}")

# model.compile(metrics=["accuracy"])
# evaluation = model.evaluate(test_ds, return_dict=True)
# for name, value in evaluation.items():
#     print(f"{name}: {value:.4f}")
    
# model.summary()
# model.make_inspector().variable_importances()
# model.save("model/dep_weather_model")
