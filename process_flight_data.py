import pandas as pd
import datetime as dt

# Read passenger departure data
# Status: Cancelled, Dep XX:XX, Dep XX:XX (XX/XX/XXXX)
pass_dep = pd.read_csv('pass_departure_data.csv')
selected_columns = ['date', 'arrival', 'time', 'flight', 'status', 'destination']
pass_dep = pass_dep[selected_columns]
# print(pass_dep)
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
        print(schedule_time_str)
    except ValueError:
        print("Invalid format for time or date")

# Read passenger arrival data
# Status: Cancelled, At gate XX:XX, At gate XX:XX (XX/XX/XXXX)
# pass_arr = pd.read_csv('pass_arrival_data.csv')
# selected_columns = ['date', 'arrival', 'time', 'flight', 'status', 'origin']
# pass_arr = pass_arr[selected_columns]
# print(pass_arr)