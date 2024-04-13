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

dep_weather = merged_dep_weather_data()
# arr_weather = merged_arr_weather_data()

uniqueLabel = np.unique(dep_weather['label']) ## 6 labels
## Cancel, Delay 5 to 30 mins, Delay 30 mins to 1 hours, Delay 1 to 2 hours, Delay more than 2 hours, On time
uniqueDate = np.unique(dep_weather['date']) #100 unique dates
uniqueAirlines = np.unique(dep_weather['airline']) #219 unique value
uniqueDestination = np.unique(dep_weather['destination']) #122 unique destination
uniqueCondition = np.unique(dep_weather['conditions']) #6 weather conditions

## Count label by date
# label_count_by_date = pd.DataFrame(columns=uniqueLabel, index=uniqueDate)
# for date in uniqueDate:
#     filtered_data = dep_weather[dep_weather['date'] == date]
#     label_counts = filtered_data['label'].value_counts()
#     label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
#     label_count_by_date.loc[date] = label_counts
# label_count_by_date.to_csv('./table/label_by_date.csv')

# fig, ax = plt.subplots()
# for labelStr in uniqueLabel:
#     ax.plot(label_count_by_date.index, label_count_by_date[labelStr], label = labelStr)
# ax.set_xlabel("Date")
# ax.set_ylabel("Count")
# ax.set_title("Different status by date")
# ax.tick_params(axis='x', which='major', rotation=90)
# plt.legend()
# plt.tight_layout()
# plt.savefig('./pics/status_by_date.png')

## Count label by wind speed
# dep_weather['wind_label'] = dep_weather.apply(label_windspeed, axis=1)
# status_by_wind = pd.DataFrame(columns=uniqueLabel, index=wind_labels)
# for wind in wind_labels:
#     filtered_data = dep_weather[dep_weather['wind_label'] == wind]
#     label_counts = filtered_data['label'].value_counts()
#     label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
#     status_by_wind.loc[wind] = label_counts
#     status_by_wind.to_csv('./table/status_by_wind.csv')

## Count label by flight mode
# dep_weather['airline_label'] = dep_weather.apply(label_airline_type, axis=1)
# status_by_flight_mode = pd.DataFrame(columns=uniqueLabel, index=flight_mode)
# for mode in flight_mode:
#     filtered_data = dep_weather[dep_weather['airline_label'] == mode]
#     label_counts = filtered_data['label'].value_counts()
#     label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
#     status_by_flight_mode.loc[mode] = label_counts
#     status_by_flight_mode.to_csv('./table/status_by_flight_mode.csv')

# status_by_destination = pd.DataFrame(columns=uniqueLabel, index=uniqueDate)
# for destination in uniqueDestination:
#     for dateStr in uniqueDate:
#         filteredData = dep_weather[(dep_weather['date'] == dateStr) & (dep_weather['destination'] == destination)]
#         label_counts = filteredData['label'].value_counts()
#         label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
#         status_by_destination.loc[dateStr] = label_counts
#         status_by_destination.to_csv(('./table/flight_status_{}.csv').format(destination))

#         fig, ax = plt.subplots()
#         for labelStr in uniqueLabel:
#             ax.plot(status_by_destination.index, status_by_destination[labelStr], marker='o', markersize=4, label = labelStr)
#         ax.set_xlabel("Date")
#         ax.set_ylabel("Count")
#         ax.set_title(("Flight status from Hong Kong to {}").format(destination))
#         ax.tick_params(axis='x', which='major', rotation=90)
#         plt.legend()
#         plt.tight_layout()
#         plt.savefig(('./pics/flight_status_{}').format(destination))
#         plt.close()

status_by_condition = pd.DataFrame(columns=uniqueLabel, index=uniqueCondition)
for condition in uniqueCondition:
    filtered_data = dep_weather[dep_weather['conditions']==condition]
    label_counts = filtered_data['label'].value_counts()
    label_counts = label_counts.reindex(uniqueLabel, fill_value=0)
    status_by_condition.loc[condition] = label_counts
    status_by_condition.to_csv('./table/status_by_condition.csv')