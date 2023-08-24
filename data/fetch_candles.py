import finnhub
import pandas as pd
import numpy as np
from datetime import datetime

finnhub_client = finnhub.Client(api_key="chq45fpr01qt7cgvsprgchq45fpr01qt7cgvsps0")

#The stock symbol
stock = 'AAPL'

#UNIX timestamp (UTC) fitting 
start_date = datetime(2010, 1, 1)
end_date = datetime(2023, 8, 1)
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())
 
#Transfrom Dict to DataFrame
df1 = finnhub_client.stock_candles(stock, 'D', start_timestamp, end_timestamp)
df = pd.DataFrame(df1)
df.drop(['s'], axis=1, inplace=True)
#Save as csv
print(df)
df.to_csv(f'data/{stock}_candles.csv', index=False)