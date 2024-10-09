import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data = np.loadtxt('task9.csv', delimiter =',', dtype = str, skiprows = 1)

dates = data[:,0]
META = data[:,1].astype(float)
AAPL = data[:,2].astype(float)
AMZN = data[:,3].astype(float)
NFLX = data[:,4].astype(float)
NVDA = data[:,5].astype(float)
GOOGL = data[:,6].astype(float)

dates = [datetime.strptime(date, '%d/%m/%Y') for date in dates]

plt.figure(figsize=(12,6))

plt.plot(dates, META, label = 'META +184.22%', color = 'blue')
plt.plot(dates, AAPL, label = 'AAPL +126.56%', color = 'grey')
plt.plot(dates, AMZN, label = 'AMZN +141.12%', color = 'black')
plt.plot(dates, NFLX, label = 'NFLX +193.34%', color = 'red')
plt.plot(dates, NVDA, label = 'NVDA +290.15%', color = 'green')
plt.plot(dates, GOOGL, label = 'GOOGL +119.06%', color = 'yellow')

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('FAANNG Performance')
plt.legend()

plt.show()