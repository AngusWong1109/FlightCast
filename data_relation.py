import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from merge_data import merged_dep_weather_data, merged_arr_weather_data

wind_labels = ['Calm (0-5.5 kmph)', 'Light Breeze (5.5-11 kmph)', 'Moderate Breeze (11-16 kmph)', 'Fresh Breeze (16-22 kmph)', 'Strong Breeze (22-28 kmph)', 'Gale (>28 kmph)']
flight_mode = ['codeshare flight', 'interline flight']

def label_windspeed(row):
    if float(row['windspeed']) > 28:
        return wind_labels[5]
    elif float(row['windspeed']) > 22:
        return wind_labels[4]
    elif float(row['windspeed']) > 16:
        return wind_labels[3]
    elif float(row['windspeed']) > 11:
        return wind_labels[2]
    elif float(row['windspeed']) > 5.5:
        return wind_labels[1]
    else:
        return wind_labels[0]
    
def label_airline_type(row):
    if(len(row['airline'].split()) > 1):
        return flight_mode[0]
    else:
        return flight_mode[1]

## Count label by date
def count_label_by_date(df, uniqueDate, uniqueLabel, dir):
    label_count_by_date = pd.DataFrame(columns=uniqueLabel, index=uniqueDate)
    for date in uniqueDate:
        filtered_data = df[df['date'] == date]
        label_counts = filtered_data['label'].value_counts()
        label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
        label_count_by_date.loc[date] = label_counts
    label_count_by_date.to_csv(('./table/{}_label_by_date.csv').format(dir))

    fig, ax = plt.subplots(figsize=(15,6))
    for labelStr in uniqueLabel:
        ax.plot(label_count_by_date.index, label_count_by_date[labelStr], label = labelStr)
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    ax.set_title("Different status by date")
    ax.tick_params(axis='x', which='major', rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig(('./pics/{}_status_by_date.png').format(dir))

## Count label by wind speed
def count_label_by_wind(df, uniqueLabel, dir):
    df['wind_label'] = df.apply(label_windspeed, axis=1)
    status_by_wind = pd.DataFrame(columns=uniqueLabel, index=wind_labels)
    for wind in wind_labels:
        filtered_data = df[df['wind_label'] == wind]
        label_counts = filtered_data['label'].value_counts()
        label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
        status_by_wind.loc[wind] = label_counts
        status_by_wind.to_csv(('./table/{}_status_by_wind.csv').format(dir))

## Count label by flight mode
def count_label_by_flight_mode(df, uniqueLabel, dir):
    df['airline_label'] = df.apply(label_airline_type, axis=1)
    status_by_flight_mode = pd.DataFrame(columns=uniqueLabel, index=flight_mode)
    for mode in flight_mode:
        filtered_data = df[df['airline_label'] == mode]
        label_counts = filtered_data['label'].value_counts()
        label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
        status_by_flight_mode.loc[mode] = label_counts
        status_by_flight_mode.to_csv(('./table/{}_status_by_flight_mode.csv').format(dir))

##Count label by place
def count_label_by_destination(df, uniqueLabel, uniqueDestination, uniqueDate):
    status_by_destination = pd.DataFrame(columns=uniqueLabel, index=uniqueDate)
    for destination in uniqueDestination:
        for dateStr in uniqueDate:
            filteredData = df[(df['date'] == dateStr) & (df['destination'] == destination)]
            label_counts = filteredData['label'].value_counts()
            label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
            status_by_destination.loc[dateStr] = label_counts
            status_by_destination.to_csv(('./table/dep/flight_status_{}.csv').format(destination))

            fig, ax = plt.subplots(figsize=(15,6))
            for labelStr in uniqueLabel:
                ax.plot(status_by_destination.index, status_by_destination[labelStr], marker='o', markersize=4, label = labelStr)
            ax.set_xlabel("Date")
            ax.set_ylabel("Count")
            ax.set_title(("Flight status from Hong Kong to {}").format(destination))
            ax.tick_params(axis='x', which='major', rotation=90)
            plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
            plt.tight_layout()
            plt.savefig(('./pics/dep/flight_status_{}').format(destination))
            plt.close()

def count_label_by_origin(df, uniqueLabel, uniqueOrigin, uniqueDate):
    status_by_origin = pd.DataFrame(columns=uniqueLabel, index=uniqueDate)
    for origin in uniqueOrigin:
        for dateStr in uniqueDate:
            filteredData = df[(df['date'] == dateStr) & (df['origin'] == origin)]
            label_counts = filteredData['label'].value_counts()
            label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
            status_by_origin.loc[dateStr] = label_counts
            status_by_origin.to_csv(('./table/arr/flight_status_{}.csv').format(origin))

            fig, ax = plt.subplots(figsize=(15,6))
            for labelStr in uniqueLabel:
                ax.plot(status_by_origin.index, status_by_origin[labelStr], marker='o', markersize=4, label = labelStr)
            ax.set_xlabel("Date")
            ax.set_ylabel("Count")
            ax.set_title(("Flight status from {}").format(origin))
            ax.tick_params(axis='x', which='major', rotation=90)
            plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
            plt.tight_layout()
            plt.savefig(('./pics/arr/flight_status_{}').format(origin))
            plt.close()

def count_label_by_condition(df, uniqueLabel, uniqueCondition, dir):
    status_by_condition = pd.DataFrame(columns=uniqueLabel, index=uniqueCondition)
    for condition in uniqueCondition:
        filtered_data = df[df['conditions']==condition]
        label_counts = filtered_data['label'].value_counts()
        label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
        status_by_condition.loc[condition] = label_counts
        status_by_condition.to_csv(('./table/{}_status_by_condition.csv').format(dir))

dep_weather = merged_dep_weather_data()

depUniqueLabel = np.unique(dep_weather['label']) ## 6 labels
## Cancel, Delay 5 to 30 mins, Delay 30 mins to 1 hours, Delay 1 to 2 hours, Delay more than 2 hours, On time
depUniqueDate = np.unique(dep_weather['date']) #100 unique dates
depUniqueAirlines = np.unique(dep_weather['airline']) #219 unique value
depUniqueDestination = np.unique(dep_weather['destination']) #122 unique destination
depUniqueCondition = np.unique(dep_weather['conditions']) #6 weather conditions
DEP_DIR = 'dep'

count_label_by_date(dep_weather, depUniqueDate, depUniqueLabel, DEP_DIR)
count_label_by_wind(dep_weather, depUniqueLabel, DEP_DIR)
count_label_by_flight_mode(dep_weather, depUniqueLabel, DEP_DIR)
count_label_by_destination(dep_weather, depUniqueLabel, depUniqueDestination, depUniqueDate)
count_label_by_condition(dep_weather, depUniqueLabel, depUniqueCondition, DEP_DIR)

arr_weather = merged_arr_weather_data()

arrUniqueLabel = np.unique(arr_weather['label']) ## 6 labels
## Cancel, Delay 5 to 30 mins, Delay 30 mins to 1 hours, Delay 1 to 2 hours, Delay more than 2 hours, On time
arrUniqueDate = np.unique(arr_weather['date']) #100 unique dates
arrUniqueAirlines = np.unique(arr_weather['airline'])
arrUniqueOrigin = np.unique(arr_weather['origin'])
arrUniqueCondition = np.unique(arr_weather['conditions']) #6 weather conditions
ARR_DIR = 'arr'

count_label_by_date(arr_weather, arrUniqueDate, arrUniqueLabel, ARR_DIR)
count_label_by_wind(arr_weather, arrUniqueLabel, ARR_DIR)
count_label_by_flight_mode(arr_weather, arrUniqueLabel, ARR_DIR)
count_label_by_origin(arr_weather, arrUniqueLabel, arrUniqueOrigin, arrUniqueDate)
count_label_by_condition(arr_weather, arrUniqueLabel, arrUniqueCondition, ARR_DIR)