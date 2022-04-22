#import libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
from sklearn.preprocessing import StandardScaler as sc
from sklearn.ensemble import RandomForestClassifier

###read all data

#X_test = pd.read_csv("data/test.csv");
#X_trin = pd.read_csv("data/train.csv");
X = pd.read_csv(r'C:\Users\Admin\PycharmProjects\interns_day\data\train.csv')
X_t = pd.read_csv(r'C:\Users\Admin\PycharmProjects\interns_day\data\test.csv')

y_train = X['cpu_usage']
X_train = X.drop(['cpu_usage', 'timestamp'], axis=1)
X_test = X_t.drop(['timestamp'], axis=1)

X['timestamp'] = pd.to_datetime(X['timestamp'])
X_t['timestamp'] = pd.to_datetime(X_t['timestamp'])

X_train['year'], X_train['month'], X_train['day'], X_train['hours'], X_train['minutes'], X_train['seconds'] = X['timestamp'].apply(lambda x: x.year), X['timestamp'].apply(lambda x: x.month), X['timestamp'].apply(lambda x: x.day), X['timestamp'].apply(lambda x: x.hour), X['timestamp'].apply(lambda x: x.minute), X['timestamp'].apply(lambda x: x.second)


print(X_train.isna().sum(), X_test.isna().sum())
print(X_train.isnull().sum(), X_test.isnull().sum())
print(X_train.dtypes, X_test.dtypes)
#answer_timestamp = X_test['timestamp']
#answer_id = X_test['Unnamed: 0']

#Lets see plots
"""
#plt.plot(X['id'],X["cpu_usage"])
#plt.plot_date(X['cpu_usage'], X_train['hours'])
#plt.plot_date(X['cpu_usage'], X['cpu_cores'])
#plt.plot_date(X['number_of_errors'], X['cpu_usage'])
#plt.plot_date(X['response_time'], X['cpu_usage'])
#plt.plot_date(X['memory_usage'], X['cpu_usage'])
#plt.plot( X['number_of_requests'],X['cpu_usage'])
#plt.waitforbuttonpress()
"""

X_train = X_train.drop(['year', 'month', 'day', 'minutes', 'seconds', 'response_time', 'number_of_errors'], axis=1)
X_test['year'] = X_t['timestamp'].apply(lambda x: x.year)
X_test = X_test.drop(['response_time', 'number_of_errors'], axis=1)
#changes for optimalization
#no need to lable objects
#standard scaler ->norm by features
X_train = sc().fit_transform(X_train)

#I wasnt sure bout clasifire or regretion should be thats why i choose random forest
clf = RandomForestClassifier()
clf.fit(X_train,y_train.to_numpy())



