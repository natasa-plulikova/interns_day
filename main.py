# Project of Stefan Otto Novak

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('train.csv')
data.head()


plt.figure(figsize=(36, 15))
plt.scatter(data['response_time'], data['cpu_usage'], c= '#DDBEA9')
plt.show()