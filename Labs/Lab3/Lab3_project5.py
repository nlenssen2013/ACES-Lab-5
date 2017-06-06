#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:54:51 2017

@author: ssroka
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


desiredAttrib = ["year","number"]
fileName = "rebnut_US-VA_1-110.csv"
baseYear = 1900

data = pd.read_csv(fileName)
    

data.plot(y="number",x="year")

array2D = data.as_matrix(columns=["number","year"])
array2D[:,1] +=baseYear 

print array2D
## ----------- Post Processing Data ---------------------------------------
mean_number = data.number.mean()
stddev_number = data.number.std()
maxNum_obs = data.number.max()
print "mean is  %3.5f and the standard deviation is %3.5f" % (mean_number, stddev_number)
print "Max number of observations %3.0f in the year %i" % (maxNum_obs,array2D[np.argmax(array2D[:,1]),0])


fig2 = plt.figure()

plt.plot(array2D[:,1],array2D[:,0])
plt.ylabel("number")
plt.xlabel("year")
plt.title('Number of birds')
plt.show()
#


    






