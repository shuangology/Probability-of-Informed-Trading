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


Two PIN estimation methods are included in the code, the first is the Easley, Hvidkjaer, and O’Hara (EHO, 2010)  method as the following:



![屏幕快照 2020-08-19 下午12 29 35](https://user-images.githubusercontent.com/43864477/90629661-aba40600-e217-11ea-8830-135333a771dd.png)



The other is using the following joint likelihood function in MLE to overcome floating-point exception, from Lin and Ke (LK, 2011) 



![屏幕快照 2020-08-19 下午12 12 05](https://user-images.githubusercontent.com/43864477/90628763-18b69c00-e216-11ea-9445-a9267074b1e5.png)



Reference: 

Easley, D., Hvidkjaer, S., O’Hara, M., 2010. Factoring information into returns. Journal of Financial and Quantitative Analysis 45, 293–309.

Yan Y, Zhang S. An improved estimation method and empirical properties of the probability of informed trading[J]. Journal of Banking &amp; Finance, 2012, 36(2): 454-467.

Lin, H.W., Ke, W.C., 2011. A computing bias in estimating the probability of informed trading. Journal of Financial Markets 14, 625–640.
