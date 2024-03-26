import pandas as pd
import datetime as dt

def label_data(row):
    if row['actual time diff'] > 120:
            return 'Delayed more than 2 hours'
    elif row['actual time diff'] > 60:
        return 'Delayed 1 to 2 hours'
    elif row['actual time diff'] > 30:
        return 'Delayed 30 mins to 1 hours'
    elif row['actual time diff'] > 5:
        return 'Delayed 5 to 30 mins'
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
    df['actual time diff'] = None
    df['label'] = None
    
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
