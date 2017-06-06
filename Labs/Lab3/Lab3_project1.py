#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:54:51 2017

@author: ssroka
"""
import numpy as np
import matplotlib.pyplot as plt


def fofx(x):
    f = 1./(np.pi*(1+np.power(x,2)))
    return(f)


    
x = np.linspace(-4.,4.,401)

y = fofx(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lab 3, Project 1")
plt.show()



