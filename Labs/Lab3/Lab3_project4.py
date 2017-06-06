#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:54:51 2017

@author: ssroka
"""
import numpy as np
import matplotlib.pyplot as plt



    
def getYear(fileName,baseYear,attrib=["year","number"]):
    "takes in fileName and starting year and outputs list of years and"
    " list of numbers"
    try:
        fid = open(fileName)
    except  IOError:
        raise ValueError("Data file does not exist")
    else:
        titles = fid.readline().split(",")
        
        # create a dictionary of column numbers and field values
        dataDict = {}
        for i in range(0,len(titles)):
            dataDict[titles[i].rstrip("\r\n")]=i
        col2Return = [dataDict[x] for x in attrib]
        
        # read data file
        subArrays = np.transpose(np.loadtxt(fid, delimiter=',', usecols=(col2Return), unpack=True))
        
        
        # if one of the desired attributes was 'year'
        if "year" in attrib:
                col_year = dataDict["year"]
                subArrays[:,col2Return.index(col_year)] += baseYear
    
        fid.close()

    return subArrays

desiredAttrib = ["year","number"]

outputArrays = getYear("rebnut_US-VA_1-110.csv",1900,desiredAttrib)
for i in range(0,len(desiredAttrib)):
    exec("%s_array = outputArrays[:,%d ]" % (desiredAttrib[i] , i) )
    
    
# ----------- Post Processing Data ---------------------------------------
mean_number = np.mean(number_array)
stddev_number = np.std(number_array)
maxNum_obs = np.amax(number_array)
print "mean is  %3.5f and the standard deviation is %3.5f" % (mean_number, stddev_number)
print "Max number of observations %3.0f in the year %i" % (maxNum_obs,year_array[np.argmax(number_array)])

# ----------- write results file ---------------------------------------
fid = open("resultsFile.txt","w+")
for i in range(0,len(number_array)):
    str_2_write = "%d, %3.5f\n" % (year_array[i],number_array[i])
    fid.write(str_2_write)

fid.close()
#
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
    






