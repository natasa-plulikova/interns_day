
from asyncio.windows_events import NULL
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import time
import sys




#defining values that will count as error fields
missing_values = [0,0.0,NULL]
#opening csv with pandas
df = pd.read_csv("data/test.csv", na_values = missing_values)





print("\n***Number of rows and cols***")
print(df.shape)

print("\n***Data types***\n")
print(df.dtypes)
df.describe()

print("\n")
#print(df.columns[0]) #checking the id
#print(df.iloc[1]) ##acessing a desired line in file
print("\n***Renaming the first col to id and printig first few rows, also deleting timestamp***\n")
#adding id
df.rename(
    columns=({ 'Unnamed: 0': 'id'}), 
    inplace=True,
)
df.drop('timestamp', inplace=True, axis=1) ##deleting timestamp
print(df.head()) ##print first few rows




##checking if any data wasnt inserted
print("\n***Number of paremters equal to null or zero: ***\n")
print("ids "+str(df['id'].isnull().sum()))
#print("timestamps equal "+str(df['timestamp'].isnull().sum()))
print("number_of_requests "+str(df['number_of_requests'].isnull().sum()))
print("number_of_errors "+str(df['number_of_errors'].isnull().sum()))
print("response_time "+str(df['response_time'].isnull().sum()))
print("cpu_cores "+str(df['cpu_cores'].isnull().sum()))
print("memory_usage "+str(df['memory_usage'].isnull().sum()))

print("\n***Additional tests***\n")
print("Lines where number of requests=0 and another list represents lines where response_time to that request is also 0\n")


test_dic={  #making library to save data
}

test_dic=df['number_of_requests'].isnull()
num_of_request_zero_list=[]
for key,value in test_dic.items():
	if(value==True):
            num_of_request_zero_list.append(key) ##if true(data 0 or null) append to dictionary



##not ids but num of line in .csv file
print(num_of_request_zero_list)


test_dic=df['response_time'].isnull()

num_of_request_zero_list=[]

for key,value in test_dic.items():
    
	if(value==True):
            num_of_request_zero_list.append(key)
    
    
print(num_of_request_zero_list)


##.info
##therefore if requests=0, response time to that request=0
print("Therefore if requests=0, response time to that request is also 0\n")



##Data exploration
##i am ploting the relationship between response_time and number_of errors



df2=df[['number_of_errors','response_time']]
res = seaborn.lineplot(x='response_time', y='number_of_errors', data=df2)

plt.show()





