from requests import get
import pandas as pd
import numpy as np

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Hong%20Kong%20International%20Airport/2024-03-19/2024-03-20?unitGroup=metric&include=hours&key=ZDLURKHWM6GZRFDUSAL75YSWN&contentType=csv'
response = get(url)
csv_file = open('weather_data.csv', 'wb')
csv_file.write(response.content)
csv_file.close()