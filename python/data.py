import json
import http.client
import urllib.request as request
import os

 #keys of dictionaries in results:
        #volume
        #low
        #close
        #tradingDay
        #timestamp
        #open
        #high
        #symbol

stocks = ["GOOG","AAPL","IBM","ACN","AAN","AER","ACY","AL","AYR","ALLY","AGO","CAR","BOXC","COF","CIT","CCR","CSH","CCCR","CPSS"]
for stock in stocks:
    print(stock)
    url = "http://marketdata.websol.barchart.com/getHistory.json?key=97ae9545154851a7c83d89525fbb5d56&symbol="+stock+"&type=minutes&interval=5&startDate=20160411000000&endDate=20160424000000"
    f = request.urlopen(url)
    jsonstr = f.read().decode("utf-8")
    jsondata = json.loads(jsonstr)
    results = jsondata['results'] #results is a list containing dictionaries
    path = '../testdata/' + stock + '.txt'
    with open(path, 'w') as out:
        for result in results:
            out.write(str(result['symbol']) + " " + str(result['timestamp']) +" " + str(result['close']) + "\n")
