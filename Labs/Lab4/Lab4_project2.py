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
    list_of_birds[i] = Bird(df.ix[i,0],np.array(df.ix[i,1:].tolist()))

plt.plot(years,list_of_birds[df[df.Species=='BlueJay'].index[0]].observations)
plt.show()
plt.xlabel('years')
plt.ylabel('Blue Jay')









