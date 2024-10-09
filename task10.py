import csv
import matplotlib.pyplot as plt
from datetime import datetime






plt.plot(dates, META, color = 'blue', label = 'META')
plt.plot(dates, AAPL, color = 'black', label = 'AAPL')
plt.plot(dates, AMZN, color = 'green', label = 'AMZN')
plt.plot(dates, NFLX, color = 'red', label = 'NFLX')
plt.plot(dates, NVDA, color = 'magenta', label = 'NVDA')
plt.plot(dates, GOOGL, color = 'orange', label = 'GOOGL')

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('FAANNG Performance')
plt.legend()