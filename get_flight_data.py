from requests import get
import pandas as pd
from datetime import datetime, timedelta
import os

passen_arr_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={}&arrival=true&cargo=false&lang=en'
cargo_arr_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={}&arrival=true&cargo=true&lang=en'
passen_dep_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={}&arrival=false&cargo=false&lang=en'
cargo_dep_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={}&arrival=false&cargo=true&lang=en'

# Fetch data at most previous 90 days or next 14 days
start_date = datetime(2024,3,26)
end_date = datetime(2024,3,31)
if os.path.exists('pass_arrival_data.csv'):
    pass_arr_total_df = pd.read_csv('pass_arrival_data.csv')
    pass_dep_total_df = pd.read_csv('pass_departure_data.csv')
    cargo_arr_total_df = pd.read_csv('cargo_arrival_data.csv')
    cargo_dep_total_df = pd.read_csv('cargo_departure_data.csv')
else:
    pass_arr_total_df = pd.DataFrame()
    pass_dep_total_df = pd.DataFrame()
    cargo_arr_total_df = pd.DataFrame()
    cargo_dep_total_df = pd.DataFrame()

while start_date <= end_date:
    # Get passenger arrival data
    response = get(passen_arr_url.format(start_date.strftime('%Y-%m-%d')))
    arr_data = response.json()
    arr_df = pd.DataFrame(arr_data[0])
    df_list = pd.json_normalize(arr_df['list'])
    df_list['origin'] = df_list['origin'].str[0]
    arr_df = pd.concat([arr_df.iloc[:, :3], df_list], axis=1)
    pass_arr_total_df = pd.concat([pass_arr_total_df, arr_df], axis=0)
    
    # Get passenger departure data
    response = get(passen_dep_url.format(start_date.strftime('%Y-%m-%d')))
    dep_data = response.json()
    dep_df = pd.DataFrame(dep_data[0])
    df_list = pd.json_normalize(dep_df['list'])
    df_list['destination'] = df_list['destination'].str[0]
    dep_df = pd.concat([dep_df.iloc[:, :3], df_list], axis=1)
    pass_dep_total_df = pd.concat([pass_dep_total_df, dep_df], axis=0)

    # Get cargo arrival data
    response = get(cargo_arr_url.format(start_date.strftime('%Y-%m-%d')))
    cargo_arr_data = response.json()
    cargo_arr_df = pd.DataFrame(cargo_arr_data[0])
    df_list = pd.json_normalize(cargo_arr_df['list'])
    cargo_arr_df = pd.concat([cargo_arr_df.iloc[:, :3], df_list], axis=1)
    cargo_arr_total_df = pd.concat([cargo_arr_total_df, cargo_arr_df], axis=0)

    #Get cargo departure data
    response = get(cargo_dep_url.format(start_date.strftime('%Y-%m-%d')))
    cargo_dep_data = response.json()
    cargo_dep_df = pd.DataFrame(cargo_dep_data[0])
    df_list = pd.json_normalize(cargo_dep_df['list'])
    df_list['destination'] = df_list['destination'].str[0]
    cargo_dep_df = pd.concat([cargo_dep_df.iloc[:, :3], df_list], axis=1)
    cargo_dep_total_df = pd.concat([cargo_dep_total_df, cargo_dep_df], axis=0)

    start_date = start_date + timedelta(days=1)
arr_data_file = pass_arr_total_df.to_csv('pass_arrival_data.csv', index=False)
dep_data_file = pass_dep_total_df.to_csv('pass_departure_data.csv', index=False)
cargo_arr_data_file = cargo_arr_total_df.to_csv('cargo_arrival_data.csv', index=False)
cargo_dep_data_file = cargo_dep_total_df.to_csv('cargo_departure_data.csv', index=False)
