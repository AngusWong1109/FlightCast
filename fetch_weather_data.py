from requests import get
from datetime import datetime, timedelta

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Hong%20Kong%20International%20Airport/{}/{}?unitGroup=metric&include=hours&key=3TX3Y9V92EQVZ7SG4ZT6PKEDW&contentType=csv'
start_date = datetime(2023,12,23)
end_date = datetime(2024,3,20)
csv_file = open('weather_data.csv', 'ab')

while start_date < end_date:
    next_date = start_date + timedelta(days=1)
    response = get(url.format(start_date.strftime('%Y-%m-%d'), next_date.strftime('%Y-%m-%d')))
    csv_file.write(response.content)
    start_date = next_date

csv_file.close()