import datetime
import pandas_datareader.data as web



style.use('fivethirtyeight')

start = datetime.datetime(2018, 4, 1)
end = datetime.datetime(2018, 4, 20)
sf = web.DataReader("SBUX", 'morningstar', start, end)
sf.reset_index(inplace=True)
sf.set_index("Date", inplace=True)
sf = sf.drop("Symbol", axis=1)

print(sf.head(10))