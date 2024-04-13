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
X = X.to_numpy()
y = y.to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y)

dep_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train, y_train)
y_pred = dep_model.predict(X_test)
y_score = dep_model.predict_proba(X_test)
cm = confusion_matrix(y_test, y_pred)
orig_accuracy = dep_model.score(X_test, y_test)
# print("Departure model: ")
# print(orig_accuracy)
# print(cm)

# ## Leave-One-Out Influence
# n = 1000
# removeData = [] #To ensure that we are not removing any data that we have removed before
# influence = np.zeros((n, 4))
# for x in range(X_train.shape[0]):
#     removeData.append(False)
# for i in range(n):    
#     #restore dataset
#     modified_Xtrain = X_train
#     modified_Ytrain = y_train
#     rmd = random.randint(0,len(modified_Xtrain)-1)
#     while(removeData[rmd] == True):
#         rmd = random.randint(0,len(modified_Xtrain)-1)
#     removeData[rmd] = True    
#     print('index = ', rmd)
#     removeData.append(rmd)
#     #Removing data from both X_train and Y_train
#     modified_Xtrain = np.delete(modified_Xtrain, rmd, axis=0)
#     modified_Ytrain = np.delete(modified_Ytrain, rmd, axis=0)
#     #Build the model after removing the training data
#     new_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(modified_Xtrain, modified_Ytrain)
#     #Find the accuracy rate
#     new_accuracy = new_model.score(X_test, y_test)
#     print("The score of ", i+1, "th run is ", new_accuracy)
#     influence_score = new_accuracy - orig_accuracy
#     influence[i][0] = rmd
#     influence[i][1] = orig_accuracy
#     influence[i][2] = new_accuracy
#     influence[i][3] = influence_score
#     print("influence score: ", influence_score)

# np.savetxt('./influence_data/dep_LOO_influence.txt', influence, delimiter=',')

## Find Shapley values
num = 10
epsilon = 0.01
data = np.concatenate((X_train, y_train[:, None]), axis=1)
size = len(data)
shapley = np.zeros(size)
for i in range(num):
    shuffled_data = np.random.permutation(data)
    X_train_shuffled = shuffled_data[:, :-1]
    Y_train_shuffled = shuffled_data[:, -1]
    model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train_shuffled[:1], Y_train_shuffled[:1])
    full_performance = model.score(X_test, Y_test)
    for j in range(1, size):
        print(i, ", ", j)
        current_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train_shuffled[:j+1], Y_train_shuffled[:j+1])
        current_performance = current_model.score(X_test, Y_test)
        if abs(current_performance - full_performance) < epsilon:
            continue
        new_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train_shuffled[:-1], Y_train_shuffled[:-1])
        new_performance = new_model.score(X_test, Y_test)
        marginal_contribution = current_performance - new_performance
        shapley[j] += marginal_contribution / (size + 1)
shapley /= 10
np.savetxt('./influence_data/dep_shapley.txt', shapley, delimiter=',')

arr_columns = ['time', 'flight_number', 'airline', 'origin', 'temp', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'windgust', 'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions', 'label']
arr_weather = arr_weather[arr_columns]
arr_encode_col = ['time', 'flight_number', 'airline', 'origin' ,'conditions', 'label']
for feather in arr_encode_col:
    le = LabelEncoder()
    arr_weather[feather] = le.fit_transform(arr_weather[feather])

X = arr_weather.iloc[:, :-1]
y = arr_weather.iloc[:, -1]
X = X.to_numpy()
y = y.to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y)

arr_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train, y_train)
y_pred = arr_model.predict(X_test)
y_score = arr_model.predict_proba(X_test)
cm = confusion_matrix(y_test, y_pred)
orig_accuracy = arr_model.score(X_test, y_test)
print("Arrival model: ")
print(orig_accuracy)
print(cm)

## Leave-One-Out Influence
# n = 1000
# removeData = [] #To ensure that we are not removing any data that we have removed before
# influence = np.zeros((n,4))
# for x in range(X_train.shape[0]):
#     removeData.append(False)
# for i in range(n):    
#     #restore dataset
#     modified_Xtrain = X_train
#     modified_Ytrain = y_train
#     rmd = random.randint(0,len(modified_Xtrain)-1)
#     while(removeData[rmd] == True):
#         rmd = random.randint(0,len(modified_Xtrain)-1)
#     removeData[rmd] = True    
#     print('index = ', rmd)
#     removeData.append(rmd)
#     #Removing data from both X_train and Y_train
#     modified_Xtrain = np.delete(modified_Xtrain, rmd, axis=0)
#     modified_Ytrain = np.delete(modified_Ytrain, rmd, axis=0)
#     #Build the model after removing the training data
#     new_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(modified_Xtrain, modified_Ytrain)
#     #Find the accuracy rate
#     new_accuracy = new_model.score(X_test, y_test)
#     print("The score of ", i+1, "th run is ", new_accuracy)
#     influence_score = new_accuracy - orig_accuracy
#     influence[i][0] = rmd
#     influence[i][1] = orig_accuracy
#     influence[i][2] = new_accuracy
#     influence[i][3] = influence_score
#     print("influence score: ", influence_score)

# np.savetxt('./influence_data/arr_LOO_influence.txt', influence, delimiter=',')

## Find Shapley values
num = 10
epsilon = 0.01
data = np.concatenate((X_train, y_train[:, None]), axis=1)
size = len(data)
shapley = np.zeros(size)
for i in range(num):
    shuffled_data = np.random.permutation(data)
    X_train_shuffled = shuffled_data[:, :-1]
    Y_train_shuffled = shuffled_data[:, -1]
    model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train_shuffled[:1], Y_train_shuffled[:1])
    full_performance = model.score(X_test, Y_test)
    for j in range(1, size):
        print(i, ", ", j)
        current_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train_shuffled[:j+1], Y_train_shuffled[:j+1])
        current_performance = current_model.score(X_test, Y_test)
        if abs(current_performance - full_performance) < epsilon:
            continue
        new_model = RandomForestClassifier(n_estimators=250, min_samples_split=10).fit(X_train_shuffled[:-1], Y_train_shuffled[:-1])
        new_performance = new_model.score(X_test, Y_test)
        marginal_contribution = current_performance - new_performance
        shapley[j] += marginal_contribution / (size + 1)
shapley /= 10
np.savetxt('./influence_data/arr_shapley.txt', shapley, delimiter=',')