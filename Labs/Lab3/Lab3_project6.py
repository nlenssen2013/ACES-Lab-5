#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:49:28 2017

@author: ssroka
"""
import numpy as np
from numpy import unravel_index
from numpy import linalg as LA
import numpy.matlib

import pandas as pd
import sys
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


topogDataFile = sys.argv[1]

print topogDataFile

data = np.loadtxt(open(topogDataFile))

flippedData = data[::-1,::]

#plt.figure()
#
lats=np.linspace(-89.5,89.5,180)
longs=np.linspace(-179.5,179.5,360)
longs=np.linspace(0.5,359.5,360)

#CS = plt.contour(longs,lats,flippedData)

#plt.show()


mountainHighEnough = unravel_index(flippedData.argmax(), flippedData.shape)
valleyLowEnough = unravel_index(flippedData.argmin(), flippedData.shape)

#plt.plot(longs[mountainHighEnough[1]],lats[mountainHighEnough[0]],'rx')
#plt.plot(longs[valleyLowEnough[1]],lats[valleyLowEnough[0]],'bo')
#plt.plot(longs[142],lats[107],'yo')


R = 6378.100 # kilometers

#R = 1
#z = np.zeros(np.shape(flippedData))


#dA = R**2*np.cos(th)*d_th*d_phi
                
#    0-----A-----1
#    |           |
#    |           |
#    C           D
#    |           |
#    |           |
#    2-----B-----3                
                
dA = 0
dV = 0
longs_rad = longs*np.pi/180  
lats_rad  = lats*np.pi/180   
                
for i in range(0,len(lats)-1):
    for j in range(0,len(longs)-1):
        
        z_test =np.array([flippedData[i,j], flippedData[i,j+1],\
                     flippedData[i+1,j], flippedData[i+1,j+1]])
        if (np.all(z_test<0)):
            x = np.matlib.repmat(longs_rad[j:j+2],1,2)[0]
            y = np.matlib.repmat(lats_rad[i:i+2],2,1).reshape((1,4),order='F')[0]
            x = x*R
            y = y*R
            z = np.array([0,0,0,0])
    
            pts = np.vstack((x,y,z))
            
            lA = LA.norm(pts[:,1]-pts[:,0])
            lB = LA.norm(pts[:,3]-pts[:,2])
            lC = LA.norm(pts[:,0]-pts[:,2])
            lD = LA.norm(pts[:,1]-pts[:,3])
            
            d_phi = np.mean([lA,lB])# long
            d_th = np.mean([lC,lD]) # lat
            
            new_dA = np.cos(np.mean([lats_rad[i],lats_rad[i+1]]))*d_phi*d_th   
                          
            dA = dA + new_dA
            dV = dV + np.absolute(np.mean(z_test))/1000*new_dA
print "The ocean surface area I compute is      % 10.2f\nthe no terrain total Earth solution is \
% 10.2f" % (dA,4*np.pi*R**2)


print "The volume of the ocean I compute is % 2.3f billion cubic km"\
% (dV/1e9)



