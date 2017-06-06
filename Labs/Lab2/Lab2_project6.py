#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 13:06:44 2017

@author: ssroka
"""



#
def getMean(observations):
    "gets mean of list of observations"
    mean = sum(observations)/len(observations)
    return mean
#    
#
def getStdDev(observations):
    "gets standard deviation"
    mu= getMean(observations)
    sig =  (float(sum([(float(x)-mu)**2 for x in observations]))/len(observations))**(0.5)
    return sig

def getMaxNum(observations,year):
    "gets maximum from list"
    maxVal = [None]*2
    maxVal[0] = max(observations)
    maxVal[1] = year[observations.index(maxVal[0])]
    
    return(maxVal)
    
def getYear(fileName,baseYear,attrib=["year","number"]):
    "takes in fileName and starting year and outputs list of years and"
    " list of numbers"

    fid = open(fileName)
    titles = fid.readline().split(",")
    dataDict = {}
    for i in range(0,len(titles)):
        dataDict[titles[i].rstrip("\r\n")]=i
                 
    col2Return = [dataDict[x] for x in attrib]
    subLists = []
    
    nxtLine = fid.readline().split(",")
    
    for line in fid:
        subLists.append([nxtLine[x] for x in col2Return])
        nxtLine = line.split(",")
    
    newlist=[None]*len(col2Return)
    for i in range(0,len(col2Return)):# create output lists
        newlist[i]=[subLists[x][i] for x in range(0,len(subLists))]
    if "year" in attrib:
            col_year = dataDict["year"]
            newlist_modYear = [int(newlist[col2Return.index(col_year)][x])+\
             baseYear for x in range(0,len(newlist[col2Return.index(col_year)]))]
            newlist[col2Return.index(col_year)] = newlist_modYear

    fid.close()

    return(newlist)

answerLists = getYear("rebnut_US-VA_1-110.csv",1900)
observations = map(lambda x: float(x), answerLists[1])
mean_number = getMean(observations)
stddev_number = getStdDev(observations)
maxNum_obs = getMaxNum(observations,answerLists[0])
print "mean is  %3.5f and the standard deviation is %3.5f" % (mean_number, stddev_number)
print "Max number of observations %3.0f in the year %i" % (maxNum_obs[0],maxNum_obs[1])

# write results file
fid = open("resultsFile.txt","w+")
for i in range(0,len(observations)):
    str_2_write = "%d, %3.5f\n" % (answerLists[0][i],observations[i])
    fid.write(str_2_write)

fid.close()


import matplotlib.pyplot as plt
fid = open("resultsFile.txt","r")
x_vals=[]
y_vals=[]
for line in fid:
    nxtLine = line.rstrip("\r\n").split(", ")
    x_vals.extend([int(nxtLine[0])])
    y_vals.extend([float(nxtLine[1])])

plt.plot(x_vals,y_vals)
plt.ylabel('number')
plt.xlabel('year')
plt.title('Number of birds')
plt.show()
fid.close()

#
    



