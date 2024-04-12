# import tensorflow_decision_forests as tfdf
# import keras
# from keras.layers import Dense, Activation
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, RocCurveDisplay, accuracy_score
from merge_data import merged_dep_weather_data, merged_arr_weather_data
from process_flight_data import process_flight_data
import pandas as pd
import numpy as np
import time
import random

dep_weather = merged_dep_weather_data()
arr_weather = merged_arr_weather_data()

dep_columns = ['time', 'flight_number', 'airline', 'destination', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
dep_weather = dep_weather[dep_columns]

dep_encode_col = ['time', 'flight_number', 'airline', 'destination' ,'conditions', 'label']
for feather in dep_encode_col:
    le = LabelEncoder()
    dep_weather[feather] = le.fit_transform(dep_weather[feather])

X = dep_weather.iloc[:, :-1]
y = dep_weather.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y)

start_time = time.time()
dep_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train, y_train)
y_pred = dep_model.predict(X_test)
y_score = dep_model.predict_proba(X_test)
cm = confusion_matrix(y_test, y_pred)
orig_accuracy = dep_model.score(X_test, y_test)
print("Departure model: ")
print(orig_accuracy)
print(cm)

n = 1000
removeData = [] #To ensure that we are not removing any data that we have removed before
influence = np.zeros((n, 4))
for x in range(X_train.shape[0]):
    removeData.append(False)
for i in range(n):    
    #restore dataset
    modified_Xtrain = X_train
    modified_Ytrain = y_train
    rmd = random.randint(0,len(modified_Xtrain)-1)
    while(removeData[rmd] == True):
        rmd = random.randint(0,len(modified_Xtrain)-1)
    removeData[rmd] = True    
    print('index = ', rmd)
    removeData.append(rmd)
    #Removing data from both X_train and Y_train
    modified_Xtrain = np.delete(modified_Xtrain, rmd, axis=0)
    modified_Ytrain = np.delete(modified_Ytrain, rmd, axis=0)
    #Build the model after removing the training data
    new_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(modified_Xtrain, modified_Ytrain)
    #Find the accuracy rate
    new_accuracy = new_model.score(X_test, y_test)
    print("The score of ", i+1, "th run is ", new_accuracy)
    influence_score = new_accuracy - orig_accuracy
    influence[i][0] = rmd
    influence[i][1] = orig_accuracy
    influence[i][2] = new_accuracy
    influence[i][3] = influence_score
    print("influence score: ", influence_score)

np.savetxt('./dep_LOO_influence.txt', influence, delimiter=',')
end_time = time.time()
print("dep used time: ", end_time - start_time)

arr_columns = ['time', 'flight_number', 'airline', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
arr_weather = arr_weather[arr_columns]
arr_encode_col = ['time', 'flight_number', 'airline', 'origin' ,'conditions', 'label']
for feather in arr_encode_col:
    le = LabelEncoder()
    arr_weather[feather] = le.fit_transform(arr_weather[feather])

X = arr_weather.iloc[:, :-1]
y = arr_weather.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y)

start_time = time.time()
arr_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train, y_train)
y_pred = arr_model.predict(X_test)
y_score = arr_model.predict_proba(X_test)
cm = confusion_matrix(y_test, y_pred)
orig_accuracy = arr_model.score(X_test, y_test)
print("Arrival model: ")
print(orig_accuracy)
print(cm)

n = 1000
removeData = [] #To ensure that we are not removing any data that we have removed before
influence = np.zeros((n,4))
for x in range(X_train.shape[0]):
    removeData.append(False)
for i in range(n):    
    #restore dataset
    modified_Xtrain = X_train
    modified_Ytrain = y_train
    rmd = random.randint(0,len(modified_Xtrain)-1)
    while(removeData[rmd] == True):
        rmd = random.randint(0,len(modified_Xtrain)-1)
    removeData[rmd] = True    
    print('index = ', rmd)
    removeData.append(rmd)
    #Removing data from both X_train and Y_train
    modified_Xtrain = np.delete(modified_Xtrain, rmd, axis=0)
    modified_Ytrain = np.delete(modified_Ytrain, rmd, axis=0)
    #Build the model after removing the training data
    new_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(modified_Xtrain, modified_Ytrain)
    #Find the accuracy rate
    new_accuracy = new_model.score(X_test, y_test)
    print("The score of ", i+1, "th run is ", new_accuracy)
    influence_score = new_accuracy - orig_accuracy
    influence[i][0] = rmd
    influence[i][1] = orig_accuracy
    influence[i][2] = new_accuracy
    influence[i][3] = influence_score
    print("influence score: ", influence_score)

np.savetxt('./arr_LOO_influence.txt', influence, delimiter=',')
end_time = time.time()
print("arr used time: ", end_time - start_time)

# X_train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(X_train, label='label')

# pass_dep_model = keras.Sequential()
# pass_dep_model.add(Dense(2048, activation='relu'))
# pass_dep_model.add(Dense(1024, activation='relu'))
# pass_dep_model.add(Dense(512, activation='relu'))
# pass_dep_model.add(Dense(256, activation='relu'))
# pass_dep_model.add(Dense(128, activation='relu'))
# pass_dep_model.add(Dense(64, activation='relu'))
# pass_dep_model.add(Dense(32, activation='relu'))
# pass_dep_model.add(Dense(16, activation='relu'))
# pass_dep_model.add(Dense(8, activation='relu'))
# pass_dep_model.add(Dense(6, activation='softmax'))

# pass_dep_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# pass_dep_model.fit(X_train, y_train, epochs=2000, batch_size=125, verbose=2)
# print(pass_dep_model.evaluate(X_test, y_test)[1])