import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import tensorflow as tf
from merge_data import merged_dep_weather_data, merged_arr_weather_data
from process_flight_data import process_flight_data

dep_weather = merged_dep_weather_data()
df_file = pd.DataFrame(dep_weather).to_csv('transformed_dep_weather.csv', index=False)

# arr_weather = merged_arr_weather_data()

# # Binarize the label column
# le = LabelEncoder()
# dep_weather['label'] = le.fit_transform(dep_weather['label'])
# # lb = LabelBinarizer()
# # arr_weather['label'] = lb.fit_transform(arr_weather['label'])

# dateTransformer = ColumnTransformer(
#     [
#         ('date_ohe', OneHotEncoder(sparse_output=False), ['date', 'time'])
#     ],
#     remainder='passthrough'
# )

# dep_weather = dateTransformer.fit_transform(dep_weather)

# df_file = pd.DataFrame(dep_weather).to_csv('transformed_dep_weather.csv', index=False)
