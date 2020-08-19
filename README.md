# Probability-of-Informed-Trading
Implementation of PIN ( Probability of Informed trading) on A-Share daily public data 



based on  Yan Y, Zhang S. An improved estimation method and empirical properties of the probability of informed trading[J]. Journal of Banking &amp; Finance, 2012, 36(2): 454-467.


By construction, the probability of informed trading (PIN) measures the proportion of trades that are likely to be motivated by private information. PIN is usually estimated with intraday data.

Due to the limitation of the data availability, we here use daily public available data to calculate A-share daily level probabiliry of informed trading.

Data is downloaded from Wind. Download of the data is implemented in WindDataGet_dailyBS.py. 

The only available buy/sell data available in Wind is the buy/sell amount of different investor types. As such, investor types and their critiria are as following:


| A_1 | A_2 | A_3 | A_4|
|----|-----|-----|-----|
|Trading Quantity exceed 1000000 CNY | Trading Quantity exceed 500000 CNY |Trading Quantity exceed 150000 CNY |Trading Quantity exceed 40000 CNY|

