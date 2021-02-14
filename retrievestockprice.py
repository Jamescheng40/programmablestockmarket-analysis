import yfinance as yf
import pandas as pd
import math

msft = yf.Ticker("TLRY")

# # get stock info
# #print(msft.info)

# # get historical market data
# hist = msft.history(period="1d")

data = msft.history(period="max",interval="1mo",start="2008-1-1")

#print(data)

#data_top = data.tail(data.shape[0])  
#rint(data.shape[0])
# # iterating the columns 
# for row in data: 
#     print(row) 
#print(data_top)

print(data)

#iterating through data annd calculate average volumn
# for i in range(data.shape[0]):
#     print(data[:i])
avg_count = 0
avg_num = 0
for i in range(data.shape[0]):
    x = float(data[i:i+1]["Volume"])
    if not(math.isnan(x)):
        avg_num = avg_num + 1
        avg_count = avg_count + x


print((avg_count/avg_num))


