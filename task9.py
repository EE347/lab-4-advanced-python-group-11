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

plt.plot(dates, META)
plt.plot(dates, AAPL)
plt.plot(dates, AMZN)
plt.plot(dates, NFLX)
plt.plot(dates, NVDA)
plt.plot(dates, GOOGL)

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('FAANNG Performance')
plt.legend()

plt.show()
