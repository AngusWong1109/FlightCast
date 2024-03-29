import pandas as pd
import datetime as dt
import ast

def label_data(row):
    if row['status'] == 'Cancelled':
        return 'Cancell'
    elif row['actual time diff'] > 120:
            return 'Delay more than 2 hours'
    elif row['actual time diff'] > 60:
        return 'Delay 1 to 2 hours'
    elif row['actual time diff'] > 30:
        return 'Delay 30 mins to 1 hours'
    elif row['actual time diff'] > 5:
        return 'Delay 5 to 30 mins'
    else:
        return 'On time'

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
    
    def parse_and_cal_diff(row):
        try:
            time_split = row['status'].split()
            if len(time_split) == 1:
                return
            if(not arrival):
                if len(time_split) > 2:
                    date_str = time_split[1] + ' ' + time_split[2]
                    status_time = dt.datetime.strptime(date_str, "%H:%M (%d/%m/%Y)")
                else:
                    date_str = row['date'] + ' ' + time_split[1]
                    status_time = dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            elif (arrival):
                if len(time_split) > 3:
                    date_str = time_split[2] + ' ' + time_split[3]
                    status_time = dt.datetime.strptime(date_str, "%H:%M (%d/%m/%Y)")
                else:
                    date_str = row['date'] + ' ' + time_split[2]
                    status_time = dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            schedule_time_str = row['date'] + ' ' + row['time']
            schedule_time = dt.datetime.strptime(schedule_time_str, "%Y-%m-%d %H:%M")
            time_diff = status_time - schedule_time
            time_diff_mins = time_diff.total_seconds() / 60
            return time_diff_mins
        except ValueError:
            print("Invalid format for time or date")
            return None

    df['actual time diff'] = df.apply(parse_and_cal_diff, axis=1)
    df['label'] = df.apply(label_data, axis=1)
    
    return df
