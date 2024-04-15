import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder
import os

def predict(data):
    data = np.array(data)
    print(os.getcwd())
    label_class_path = "C:/Users/Angus/Desktop/CMPT419Project/FlightStatusPrediction/app/src/main/python/assets/label_classes"
    model = joblib.load("C:/Users/Angus/Desktop/CMPT419Project/FlightStatusPrediction/app/src/main/python/assets/dep_model.sav")
    time_lb = LabelEncoder()
    time_lb.classes_ = np.load((label_class_path + 'dep_time.npy'))
    airline_lb = LabelEncoder()
    airline_lb.classes_ = np.load((label_class_path + 'dep_airline.npy'))
    flight_num_lb = LabelEncoder()
    flight_num_lb.classes_ = np.load((label_class_path + 'dep_flight_number.npy'))
    dest_lb = LabelEncoder()
    dest_lb.classes_ = np.load((label_class_path + 'dep_destination.npy'))
    conditions_lb = LabelEncoder()
    conditions_lb.classes_ = np.load((label_class_path + 'dep_conditions.npy'))
    label_lb = LabelEncoder()
    label_lb.classes_ = np.load((label_class_path + 'dep_label.npy'))
    
    data[0] = time_lb.transform(data[0])
    data[1] = flight_num_lb.transform(data[1])
    data[2] = airline_lb.transform(data[2])
    data[3] = dest_lb.transform(data[3])
    data[-1] = conditions_lb.transform(data[-1])
    
    y_pred = model.predict(data)
    num = np.argmax(y_pred)
    return label_lb.classes_[num]