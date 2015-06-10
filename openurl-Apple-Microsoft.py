import math

def mean(alist):
    mean = sum(alist) / len(alist)
    return mean

def standardDev(alist):
    theMean = mean(alist)
    
    sum = 0
    for item in alist:
        difference = item - theMean
        diffsq = difference ** 2
        sum = sum + diffsq
        
    sdev = math.sqrt(sum/(len(alist)-1))
    return sdev


def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDev(xlist)
    ystd = standardDev(ylist)
    num = 0.0
    for i in range(len(xlist)):
        num = num + (xlist[i]-xbar) * (ylist[i]-ybar)
    corr = num / ((len(xlist)-1) * xstd * ystd) 
    return corr

import urllib.request
#url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=AAPL') # Aple Inc.
#url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=TGT') # Target
url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=MSFT') # Microsoft

dataLen = 10
t1Data = url1.readlines()
#print( t1Data[:dataLen] )

closePrice = []
for i in range(dataLen):
    if i == 0:
        continue
    firstLine = t1Data[i].decode("utf-8").split(',')
    closePrice.append( firstLine[4] )
    print( firstLine )


print( closePrice ) # extracted close price


#t1DataAlt = [line.decode("utf-8").split(',') for line in t1Data[1:]]
#print( t1DataAlt[:3] )
