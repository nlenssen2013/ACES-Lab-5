#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:39:14 2017

@author: ssroka
"""

import numpy as np
from birdData import *
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('vabirds.csv')

years = df.columns[1:].get_values().tolist()
years = np.array([float(years[i]) for i in range(0,len(years))])

numberOfBirds = df.shape[0]

list_of_birds = [None]*numberOfBirds

for i in range(0,numberOfBirds):
    list_of_birds[i] = Bird(df.ix[i,0],df.ix[i,1:].tolist())

ansDict = list_of_birds[df[df.Species=='ChippingSparrow'].index[0]].stats(years)

plt.plot(years,list_of_birds[df[df.Species=='ChippingSparrow'].index[0]].observations)
plt.show()
plt.xlabel('years')
plt.ylabel('Chipping Sparrow')
axes = plt.gca()
plt.plot((ansDict["maxNumYr"]),(ansDict["maxNum"]),'rx')
plt.plot((ansDict["minNumYr"]),(ansDict["minNum"]),'go')
plt.plot((axes.get_xlim()),(ansDict["meanNum"],ansDict["meanNum"]),'k-')
plt.plot((axes.get_xlim()),(ansDict["medianNum"],ansDict["medianNum"]),'r-')









