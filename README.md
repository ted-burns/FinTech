# FinTech
Project for CSCI3390

## Info
In the python folder, there are two python scripts:
  data.py, which is used for collecting the data listed in the stocks array
  clean.py, which creates a dictionary full of correlations of the stocks

## Steps
1. Get the time series for the each stock
2. Turn that time series into a series of additive returns for each day at 5 minute intervals
3. For each stock, calculate the expected value for each day</li>
4. For each stock and for each day, find the difference of every value in the time series and the expected value</li>
5. With the above results, do two things:
  1. For each stock for each day, calculate the average of the above differences squared (variance for day d)
  2. For each stock (a) for each day, for each stock (b) calculate the sum of (each difference of a at time t multiplied by each difference of b at time t+1) in list item 4 (result is the covariance of a,b for day d)
6. Take the covariance matrix and the variances for each day for each set of stocks and calculate the correlation for (a,b) and (b,a)
7. For each stock(a), generative a column vector with every other stock(b) that each row is the correlation (b,a)
8. For each stock(a), generate a column vector with every other stock(b) that each row is m such that m=(correlation(b,a) x (sqrt(var(a))))

That creates the entire data model
