import pandas as pd
import numpy as np
import datetime as dt

# Read passenger departure data
# Status: Cancelled, Dep XX:XX, Dep XX:XX (XX/XX/XXXX)
pass_dep = pd.read_csv('pass_departure_data.csv')
selected_columns = ['date', 'arrival', 'time', 'flight', 'status', 'destination']
pass_dep = pass_dep[selected_columns]
pass_dep['actual time diff'] = None
pass_dep['coded_status'] = None
for i in range(pass_dep.shape[0]):
    time_split = pass_dep['status'][i].split()
    try:
        if len(time_split) == 1:
            continue
        elif len(time_split) > 2:
            date_str = time_split[1] + ' ' + time_split[2]
            status_time = dt.datetime.strptime(date_str, "%H:%M (%d/%m/%Y)")
        else:
            date_str = pass_dep['date'][i] + ' ' + time_split[1]
            status_time = dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        
        schedule_time_str = pass_dep['date'][i] + ' ' + pass_dep['time'][i]
        schedule_time = dt.datetime.strptime(schedule_time_str, "%Y-%m-%d %H:%M")
        time_diff = status_time - schedule_time

    except ValueError:
        print("Invalid format for time or date")

    time_diff_mins = time_diff.total_seconds() / 60
    pass_dep.loc[i, 'actual time diff'] = time_diff_mins
    if time_diff_mins > 120:
        pass_dep.loc[i, 'coded_status'] = 'Delayed more than 2 hours'
    elif time_diff_mins > 60:
        pass_dep.loc[i, 'coded_status'] = 'Delayed 1 to 2 hours'
    elif time_diff_mins > 30:
        pass_dep.loc[i, 'coded_status'] = 'Delayed 30 mins to 1 hours'
    elif time_diff_mins > 5:
        pass_dep.loc[i, 'coded_status'] = 'Delayed 5 to 30 mins'
    else:
        pass_dep.loc[i, 'coded_status'] = 'On time'

df_file = pass_dep.to_csv('processed_pass_dep_data.csv')

# Read passenger arrival data
# Status: Cancelled, At gate XX:XX, At gate XX:XX (XX/XX/XXXX)
pass_arr = pd.read_csv('pass_arrival_data.csv')
selected_columns = ['date', 'arrival', 'time', 'flight', 'status', 'origin']
pass_arr = pass_arr[selected_columns]
pass_arr['actual time diff'] = None
pass_arr['coded_status'] = None
for i in range(pass_arr.shape[0]):
    time_split = pass_arr['status'][i].split()
    try:
        if len(time_split) == 1:
            continue
        elif len(time_split) > 3:
            date_str = time_split[2] + ' ' + time_split[3]
            status_time = dt.datetime.strptime(date_str, "%H:%M (%d/%m/%Y)")
        else:
            date_str = pass_arr['date'][i] + ' ' + time_split[2]
            status_time = dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        
        schedule_time_str = pass_arr['date'][i] + ' ' + pass_arr['time'][i]
        schedule_time = dt.datetime.strptime(schedule_time_str, "%Y-%m-%d %H:%M")
        time_diff = status_time - schedule_time

    except ValueError:
        print("Invalid format for time or date")

    time_diff_mins = time_diff.total_seconds() / 60
    pass_arr.loc[i, 'actual time diff'] = time_diff_mins
    if time_diff_mins > 120:
        pass_arr.loc[i, 'coded_status'] = 'Delayed more than 2 hours'
    elif time_diff_mins > 60:
        pass_arr.loc[i, 'coded_status'] = 'Delayed 1 to 2 hours'
    elif time_diff_mins > 30:
        pass_arr.loc[i, 'coded_status'] = 'Delayed 30 mins to 1 hours'
    elif time_diff_mins > 5:
        pass_arr.loc[i, 'coded_status'] = 'Delayed 5 to 30 mins'
    else:
        pass_arr.loc[i, 'coded_status'] = 'On time'

df_file = pass_arr.to_csv('processed_pass_arr_data.csv')