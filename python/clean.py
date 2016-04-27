
import math
stocks_incl = ["GOOG","AAPL","IBM","ACN","AAN","AER","ACY","AL","AYR","ALLY","AGO","CAR","BOXC","COF","CIT","CCR","CSH","CCCR","CPSS"]

def quotes(stock):
    path = '../testdata/' + stock + '.txt'
    quotes = dict()
    with open(path, 'r') as f:
        for line in iter(f):
            line = f.readline()
            if line!="":
                line = line.split()
                date = line[1][:10]
                dictionary = quotes.get(date,dict())
                time = line[1][11:19]
                dictionary[time] = line[2]
                if date not in quotes:
                    quotes[date] = dictionary
    return quotes

def to_additive_return(quotes):
    ar = dict()
    for date in quotes.keys():
        quote = quotes[date]
        keys = sorted(quote)
        for i in range(1,len(keys)):
            delta = math.log(float(quote[keys[i]])) - math.log(float(quote[keys[i-1]]))
            dictionary = ar.get(date, dict())
            dictionary[i] = delta
            if date not in ar:
               ar[date] = dictionary
    return ar

def expected_val(day):
    keys = sorted(day)
    sums = float(0)
    for key in keys:
        sums += day[key]
    if len(keys) != 0:
        return (sums/len(keys))
    else:
        return 0

def variance(day,mean= False):
    if mean == False:
        mean = expected_val(day)
    keys = sorted(day)
    sums = float(0)
    for key in keys:
        sums+= (day[key] - mean)**2
    if len(keys) != 0:
        return sums/len(keys)
    else:
        return 0

def covariance(day1,day2):
    mean1=expected_val(day1)
    mean2=expected_val(day2)
    n = len(sorted(day1))
    sigma = 0.0
    for key in sorted(day1):
        if key+1 in sorted(day2):
            sigma+= (day1[key]-mean1) * (day2[key+1]-mean2)
    if n!= 0:
        return sigma/n
    else:
        return 0
    
def correlation(day1, day2):    
    mean1=expected_val(day1)
    mean2=expected_val(day2)
    var1=variance(day1,mean1)
    var2=variance(day2,mean2)
    n = len(sorted(day1))

    cov = covariance(day1,day2)
    if var1!=0 and var2!= 0:
        corr = cov / ((var1**(0.5)) * (var2**(0.5)))
    else:
        corr = 0
    return corr

def avg_correlation(series1, series2):
    avg = 0.0
    count = 0
    for day in series1:
        if day in series2:
            avg += correlation(series1[day],series2[day])
            count += 1
    if count != 0:
        return avg/count
    else:
        return 0

def name_to_timeseries(stock):
    return to_additive_return(quotes(stock))

def print_corrs(stocks=stocks_incl):
    corrs = dict()
    for stock1 in stocks:
        ar1 = name_to_timeseries(stock1)
        for date in ar1:
            del ar1[date][sorted(ar1[date])[-1]]
        for stock2 in stocks:
            ar2 = name_to_timeseries(stock2)
            for date in ar2:
                del ar2[date][1]
            corr = avg_correlation(ar1,ar2)
            print(stock1 + " " + stock2 + " " + str(corr))
            corrs[stock1 + " " + stock2] = corr
    return corrs

corrs = print_corrs()
        
