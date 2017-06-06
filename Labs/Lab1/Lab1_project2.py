#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:45:43 2017

@author: ssroka
"""
tempsC = [0]*7
tempsF = [0.]*7
for i in range(0,7):
    tempsC[i]=tempsC[i-1]+10
    tempsF[i]=tempsC[i]*9./5+32
    print tempsC[i],tempsF[i]

