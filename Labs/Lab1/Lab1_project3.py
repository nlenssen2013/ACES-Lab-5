#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:51:02 2017

@author: ssroka
"""

tempsC = range(-40,105,5)
tempsF = [tempsC_val*9./5+32 for tempsC_val in tempsC]


tempsF_alias = tempsF

tempsF_gt0=[]
for i in range(0,len(tempsF)):
    if (tempsC[i]<0 and tempsF[i]>0):
        tempsF_gt0.extend([tempsF[i]])
print "The elements which are >0 in F and <0 in C are: "
print tempsF_gt0