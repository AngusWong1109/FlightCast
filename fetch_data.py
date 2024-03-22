from requests import get
import pandas as pd
import numpy as np

passen_arr_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={:04s}-{:02s}-{:02s}&arrival=true&cargo=false&lang=en'
cargo_arr_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={:04s}-{:02s}-{:02s}&arrival=true&cargo=true&lang=en'
passen_dep_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={:04s}-{:02s}-{:02s}&arrival=false&cargo=false&lang=en'
cargo_dep_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={:04s}-{:02s}-{:02s}&arrival=false&cargo=true&lang=en'

# Get passenger arrival data
# response = get(passen_arr_url.format('2024','03','20'))
# data = response.json()
# df = pd.DataFrame(data[0])
# df_list = pd.json_normalize(df['list'])
# df_list['origin'] = df_list['origin'].str[0]
# df = pd.concat([df.iloc[:, :3], df_list], axis=1)
# print(df)

# Get passenger departure data
# response = get(passen_dep_url.format('2024','03','20'))
# data = response.json()
# df = pd.DataFrame(data[0])
# df_list = pd.json_normalize(df['list'])
# df_list['destination'] = df_list['destination'].str[0]
# df = pd.concat([df.iloc[:, :3], df_list], axis=1)
# print(df)

# Get cargo arrival data
# response = get(cargo_arr_url.format('2024','03','20'))
# data = response.json()
# df = pd.DataFrame(data[0])
# df_list = pd.json_normalize(df['list'])
# df = pd.concat([df.iloc[:, :3], df_list], axis=1)
# print(df)

#Get cargo departure data
# response = get(cargo_dep_url.format('2024','03','20'))
# data = response.json()
# df = pd.DataFrame(data[0])
# df_list = pd.json_normalize(df['list'])
# df_list['destination'] = df_list['destination'].str[0]
# df = pd.concat([df.iloc[:, :3], df_list], axis=1)
# print(df)
