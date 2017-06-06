#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 10:26:25 2017

@author: ssroka
"""

#import numpy as np
#import matplotlib.pyplot as plt
#x1 = np.linspace(0.0,5.0)
#x2 = np.linspace(0.0,2.0)
#y1 = np.cos(2* np.pi * x1)*np.exp(-x1)
#y2 = np.cos(2* np.pi * x2)
#plt.subplot(2,1,1)
#plt.plot(x1,y1,'yo-')
#plt.subplot(2,1,2)
#plt.plot(x2,y2,'r.-')
#plt.show()

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# difference of Gaussians
Z = 10.0 * (Z2 - Z1)

plt.figure()
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')

plt.show()

plt.figure()
CSf = plt.contourf(X, Y, Z)
plt.clabel(CSf, inline=1, fontsize=10)
plt.title('Simplest default with labels filled contours')

plt.show()



