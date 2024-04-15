# Introduction

This is a flight status prediction app based on data from Hong Kong International Airport (HKIA) provided by the Airport Authority Hong Kong (AA). The prediction will be divided into several categories: **On time**, **Cancelled**, **Delayed 5 to 30 minutes**, **Delayed 30 mins to 1 hours**, **Delayed 1 - 2 hours**, and **Delayed more than 2 hours**.

# Data file

Captured data is flight information from 2023/12/23 to 2024/03/25

- [`pass_departure_data.csv`](pass_departure_data.csv): Flight information of civil departure flight
- [`pass_arrival_data.csv`](pass_arrival_data.csv): Flight information of civil arrival flight

# Resources

## Library Used

- Requests
- Scikit-learn
- Pandas
- Matplotlib
- Tensorflow
- Tensorflow Lite

## Programming Language Used

- Python
- Kotlin

## Data source

- [Flight schedule information of Hong Kong International Airport (Historical), Airport Authority Hong Kong](https://data.gov.hk/en-data/dataset/aahk-team1-flight-info/resource/8f41b55c-a2ef-4963-bb25-96d8b21f3db4)
- [Visual Crossing Weather Data](https://www.visualcrossing.com/)

### Things to get in mind

- **The API provided by AA is only able to get previous 90 days and next 14 days flight information.**

# Process

## Extract-Transform-Load (ETL)

### 1. Extract: Get Data
   
- [`get_flight_data.py`](get_flight_data.py): Fetching historical flight information data for passenger departure and arrival, and cargo departure and arrival
- [`get_weather_data.py`](get_weather_data.py): Fetching historical weather data of HKIA

### 2. Transform: Process Data

- [`process_flight_data.py`](process_flight_data.py): Added Label for later training model use
- [`process_weather_data.py`](process_weather_data.py): Removed unwanted columns

### 3. Merge Data

- [`merge_data.py`](merge_data.py): Merged flight information and weather data based on given datetime

### 4. Load: Train the model

- [`model.py`](model.py): Train the AI model to predict the flight status

