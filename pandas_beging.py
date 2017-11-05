import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

#style.use('ggplot')
style.use('fivethirtyeight')

start_date = datetime.datetime(2014,1,1)
end_date = datetime.datetime(2015,1,1)

#df = web.DataReader('XOM', "yahoo", start_date, end_date)

df = web.DataReader("XOM", "yahoo", start_date, end_date)
print(df.head())
print(df.tail())

df['High'].plot()
plt.legend()
plt.show()