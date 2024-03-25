import pandas as pd
import datetime as dt

# Read passenger departure data
# Status: Cancelled, Dep XX:XX, Dep XX:XX (XX/XX/XXXX)
pass_dep = pd.read_csv('pass_departure_data.csv')
selected_columns = ['date', 'arrival', 'time', 'flight', 'status', 'destination']
pass_dep = pass_dep[selected_columns]
# print(pass_dep)
for time in pass_dep['status']:
    time_split = time.split()
    if len(time_split) == 1:
        continue
    elif len(time_split) > 2:
        date_str = time[time.find("(")+1:time.find(")")]
        print('date_str: ', date_str)
    time_str = time_split[1]
    try:
        dt_time = dt.datetime.strptime(time_str, "%H:%M")
    except ValueError:
        print("Invalid format for time or date")

# Read passenger arrival data
# Status: Cancelled, At gate XX:XX, At gate XX:XX (XX/XX/XXXX)
# pass_arr = pd.read_csv('pass_arrival_data.csv')
# selected_columns = ['date', 'arrival', 'time', 'flight', 'status', 'origin']
# pass_arr = pass_arr[selected_columns]
# print(pass_arr)