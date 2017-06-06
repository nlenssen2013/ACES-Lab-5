#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:32:13 2017

@author: ssroka
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('vabirds.csv')

years = df.columns[1:].get_values().tolist()
years = [float(years[i]) for i in range(0,len(years))]

ind_of_DW = df[df.Species=='DownyWoodpecker'].index
DW= df.ix[ind_of_DW[0] ,1:].get_values().tolist()

plt.plot(years,DW)
plt.show()
plt.xlabel('years')
plt.ylabel('Downy Woodpecker')








