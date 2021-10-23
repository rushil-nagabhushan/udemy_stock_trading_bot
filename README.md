This is a stock paper trading bot that I created as part of a Udemy course I took.

Throughout the creation of this bot, I learned not only more about Python stock trading libraries,
such as tulipy and scipy, as well as statistical analysis libraries like pandas, but also about
the intricacies of fundamental-based stock trading. I learned to use metrics such as EMA (exponential moving average) to judge whether the trend for a given asset is moving up or down at the moment, RSI (relative strength index) to calculate the volume of stock being bought or sold at a single time, and most importantly, the stochastic oscillator to judge the stock's previous trends and seeing if it has room to move between asset value lines based on past performance.

Position entry steps:

1. general trend analysis: 30 min long EMA to see if the asset is worth buying today (broad check for viability)
2. instant trend analysis: 5 min long EMA to see if the asset is worthy buying at that moment (narrower check for viability from assets screened by general trend analysis)
3. RSI analysis: another step being performed in the 5 minute window starting with instant trend analysis to check for stock's viability
4. stochastic analysis: another step being performed in the 5 minute window starting with instant trend analysis to check for stock's viability

Position exit steps:

1. check the gains made so far, and see if it meets a threshold to sell
2. or check the stochastic analysis to see if the stock is going to start losing money and we should dump it

list of assets in use: 
(TSLA,AAPL,PLTR,AMD,GE,PYPL,SONY,CSCO,ORCL,KO,GPRO,XONE,XPEV,NIO,BB,GM)