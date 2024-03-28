import pandas as pd
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
from merge_data import merged_dep_weather_data, merged_arr_weather_data

dep_weather = merged_dep_weather_data()
arr_weather = merged_arr_weather_data()
