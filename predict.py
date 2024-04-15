from requests import get
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
import datetime as dt
import ast

def dep_encoding(row):
    time_lb = LabelEncoder()
    time_lb.classes_ = np.load('./label_classes/dep_time.npy', allow_pickle=True)
    airline_lb = LabelEncoder()
    airline_lb.classes_ = np.load('./label_classes/dep_airline.npy', allow_pickle=True)
    flight_num_lb = LabelEncoder()
    flight_num_lb.classes_ = np.load('./label_classes/dep_flight_number.npy', allow_pickle=True)
    origin_lb = LabelEncoder()
    origin_lb.classes_ = np.load('./label_classes/dep_destination.npy', allow_pickle=True)
    conditions_lb = LabelEncoder()
    conditions_lb.classes_ = np.load('./label_classes/dep_conditions.npy', allow_pickle=True)
    
    time = np.array([row['time']])
    airline = np.array([row['airline']])
    flight_num = np.array([row['flight_number']])
    destination = np.array([row['destination']])
    conditions = np.array([row['conditions']])
    try:
        row['time'] = time_lb.transform(time)
        row['airline'] = airline_lb.transform(airline)
        row['flight_number'] = flight_num_lb.transform(flight_num)
        row['destination'] = origin_lb.transform(destination)
        row['conditions'] = conditions_lb.transform(conditions)
    except:
        return None
    return row

def arr_encoding(row):
    time_lb = LabelEncoder()
    time_lb.classes_ = np.load('./label_classes/arr_time.npy', allow_pickle=True)
    airline_lb = LabelEncoder()
    airline_lb.classes_ = np.load('./label_classes/arr_airline.npy', allow_pickle=True)
    flight_num_lb = LabelEncoder()
    flight_num_lb.classes_ = np.load('./label_classes/arr_flight_number.npy', allow_pickle=True)
    origin_lb = LabelEncoder()
    origin_lb.classes_ = np.load('./label_classes/arr_origin.npy', allow_pickle=True)
    conditions_lb = LabelEncoder()
    conditions_lb.classes_ = np.load('./label_classes/arr_conditions.npy', allow_pickle=True)
    
    time = np.array([row['time']])
    airline = np.array([row['airline']])
    flight_num = np.array([row['flight_number']])
    origin = np.array([row['origin']])
    conditions = np.array([row['conditions']])
    
    try:
        row['time'] = time_lb.transform(time)
        row['airline'] = airline_lb.transform(airline)
        row['flight_number'] = flight_num_lb.transform(flight_num)
        row['origin'] = origin_lb.transform(origin)
        row['conditions'] = conditions_lb.transform(conditions)
    except:
        return None
    return row

def process_flight_data(filepath, arrival = True):
    # Read data
    df = pd.read_csv(filepath)
    selected_columns = ['date', 'arrival', 'time', 'flight', 'status']
    if(arrival):
        selected_columns.append('origin')
    else:
        selected_columns.append('destination')
    df = df[selected_columns]
    df['flight_number'] = None
    df['airline'] = None
    df['actual time diff'] = None
    df['label'] = None
    
    for i in range(len(df)):
        data = ast.literal_eval(df['flight'].loc[i])
        flight_numbers = []
        airlines = []
        for flight_info in data:
            flight_number = flight_info['no']
            airline = flight_info['airline']
            flight_numbers.append(flight_number)
            airlines.append(airline)
        flight_numbers_str = ', '.join(flight_numbers)
        airlines_str = ', '.join(airlines)
        df.loc[i, 'flight_number'] = flight_numbers_str
        df.loc[i, 'airline'] = airlines_str
    return df

passen_arr_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={}&arrival=true&cargo=false&lang=en'
passen_dep_url = 'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={}&arrival=false&cargo=false&lang=en'

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Hong%20Kong%20International%20Airport?unitGroup=metric&include=hours&key=3TX3Y9V92EQVZ7SG4ZT6PKEDW&contentType=json"
today = datetime.today()
startDate = today + timedelta(days=1)
endDate = today + timedelta(days=14)

pass_arr_total_df = pd.DataFrame()
pass_dep_total_df = pd.DataFrame()
    
while startDate <= endDate:
    response = get(passen_arr_url.format(startDate.strftime('%Y-%m-%d')))
    arr_data = response.json()
    arr_df = pd.DataFrame(arr_data[0])
    df_list = pd.json_normalize(arr_df['list'])
    df_list['origin'] = df_list['origin'].str[0]
    arr_df = pd.concat([arr_df.iloc[:, :3], df_list], axis=1)
    pass_arr_total_df = pd.concat([pass_arr_total_df, arr_df], axis=0)
    
    response = get(passen_dep_url.format(startDate.strftime('%Y-%m-%d')))
    dep_data = response.json()
    dep_df = pd.DataFrame(dep_data[0])
    df_list = pd.json_normalize(dep_df['list'])
    df_list['destination'] = df_list['destination'].str[0]
    dep_df = pd.concat([dep_df.iloc[:, :3], df_list], axis=1)
    pass_dep_total_df = pd.concat([pass_dep_total_df, dep_df], axis=0)
    
    startDate = startDate + timedelta(days=1)

pass_dep_total_df.to_csv('future_dep_flight.csv', index=False)
pass_arr_total_df.to_csv('future_arr_flight.csv', index=False)

response = get(url)

weather_total = pd.DataFrame()
cols = ['date', 'time', 'temp', 'feelslike', 'humidity', 'dew', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'pressure', 'visibility', 'cloudcover', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions']
API_data = response.json()
days = API_data['days']
for day in days:
    hours = day['hours']
    for hour in hours:
        time = hour['datetime'][:5]
        weather = pd.DataFrame([day['datetime'], time, hour['temp'], hour['feelslike'], hour['humidity'], hour['dew'], hour['precip'], hour['precipprob'], hour['windgust'], hour['windspeed'], hour['winddir'], hour['pressure'], hour['visibility'], hour['cloudcover'], hour['solarradiation'], hour['solarenergy'], hour['uvindex'], hour['severerisk'], hour['conditions']]).T
        weather.columns = cols
        weather_total = pd.concat([weather_total, weather], axis=0)

pass_dep = process_flight_data('future_dep_flight.csv', False)
pass_arr = process_flight_data('future_arr_flight.csv', True)
merged_dep_weather_data = pass_dep.merge(weather_total, on=['date', 'time'])
selected_dep_columns = ['time', 'flight_number', 'airline', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'pressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions']
dep_weather = merged_dep_weather_data[selected_dep_columns]
dep_weather.columns = ['time', 'flight_number', 'airline', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions']

merged_arr_weather_data = pass_arr.merge(weather_total, on=['date', 'time'])
selected_arr_columns = ['time', 'flight_number', 'airline', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'pressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions']
arr_weather = merged_arr_weather_data[selected_arr_columns]
arr_weather.columns = ['time', 'flight_number', 'airline', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions']

arr_weather = arr_weather.apply(arr_encoding, axis=1).dropna()
model = joblib.load('./model/arr_model.sav')
label_lb = LabelEncoder()
label_lb.classes_ = np.load('./label_classes/arr_label.npy', allow_pickle=True)
y_pred = model.predict(arr_weather)
num = np.argmax(y_pred)
arr_weather['predict'] = label_lb.classes_[num]
print('arr_weather:')
print(arr_weather)

dep_weather = dep_weather.apply(dep_encoding, axis=1).dropna()
model = joblib.load('./model/dep_model.sav')
label_lb = LabelEncoder()
label_lb.classes_ = np.load('./label_classes/dep_label.npy', allow_pickle=True)
y_pred = model.predict(dep_weather)
num = np.argmax(y_pred)
dep_weather['predict'] = label_lb.classes_[num]
print('dep_weather:')
print(dep_weather)